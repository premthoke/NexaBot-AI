"""app.py — Streamlit chat UI. Talks to the FastAPI backend over HTTP."""

import uuid
import requests
import streamlit as st

API_URL = "http://localhost:8000"

st.set_page_config(page_title="AI Support Chatbot", page_icon="💬")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

with st.sidebar:
    st.header("Account")
    if st.session_state.logged_in_user:
        st.success(f"Logged in as {st.session_state.logged_in_user}")
        if st.button("Log out"):
            st.session_state.logged_in_user = None
            st.rerun()
    else:
        tab_login, tab_register = st.tabs(["Login", "Register"])

        with tab_login:
            login_user = st.text_input("Username", key="login_user")
            login_pass = st.text_input("Password", type="password", key="login_pass")
            if st.button("Log in"):
                try:
                    r = requests.post(
                        f"{API_URL}/auth/login",
                        json={"username": login_user, "password": login_pass},
                        timeout=10,
                    )
                    if r.status_code == 200:
                        st.session_state.logged_in_user = r.json()["username"]
                        st.rerun()
                    else:
                        st.error(r.json().get("detail", "Login failed"))
                except requests.exceptions.ConnectionError:
                    st.error("Can't reach the backend. Is `uvicorn backend.main:app --reload` running?")

        with tab_register:
            reg_user = st.text_input("Username", key="reg_user")
            reg_email = st.text_input("Email", key="reg_email")
            reg_pass = st.text_input("Password", type="password", key="reg_pass")
            if st.button("Create account"):
                try:
                    r = requests.post(
                        f"{API_URL}/auth/register",
                        json={"username": reg_user, "email": reg_email, "password": reg_pass},
                        timeout=10,
                    )
                    if r.status_code == 200:
                        st.success("Account created — you can log in now.")
                    else:
                        st.error(r.json().get("detail", "Registration failed"))
                except requests.exceptions.ConnectionError:
                    st.error("Can't reach the backend. Is `uvicorn backend.main:app --reload` running?")

    st.divider()
    if st.button("New conversation"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()

st.title("💬 AI Customer Support Chatbot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("meta"):
            st.caption(msg["meta"])

if user_input := st.chat_input("Ask about an order, return, payment, or product..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            r = requests.post(
                f"{API_URL}/chat",
                json={"message": user_input, "session_id": st.session_state.session_id},
                timeout=30,
            )
            r.raise_for_status()
            data = r.json()
            reply = data["reply"]
            meta_parts = []
            if data.get("detected_intent"):
                meta_parts.append(f"intent: {data['detected_intent']}")
            if data.get("extracted_entities"):
                meta_parts.append(f"entities: {data['extracted_entities']}")
            meta = " · ".join(meta_parts) if meta_parts else None

            st.markdown(reply)
            if meta:
                st.caption(meta)
            st.session_state.messages.append({"role": "assistant", "content": reply, "meta": meta})
        except requests.exceptions.ConnectionError:
            error_msg = "Can't reach the backend. Run `uvicorn backend.main:app --reload` first."
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
