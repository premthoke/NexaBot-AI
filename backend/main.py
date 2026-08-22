"""
main.py

The FastAPI application entrypoint. Run with:
    uvicorn backend.main:app --reload

`--reload` restarts the server automatically when you save a file --
handy during development, remove it in production.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.routers import chat, auth

app = FastAPI(
    title="AI Customer Support Chatbot API",
    description="NLP + LLM powered customer support backend.",
    version="0.1.0",
)

# CORS: browsers block cross-origin requests by default. Streamlit
# (Phase 4) runs on a different port (e.g. localhost:8501) than this API
# (e.g. localhost:8000), so without this, the browser would reject the
# frontend's calls to the backend. Wide open ("*") is fine for local
# development; you'd restrict this to a specific domain in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Every router gets "mounted" here. chat.router already has prefix="/chat"
# set internally, so its POST route becomes POST /chat.
app.include_router(chat.router)
app.include_router(auth.router)

# Mount the frontend directory so index.html and assets are served as static files.
_FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")
app.mount("/static", StaticFiles(directory=_FRONTEND_DIR), name="static")


@app.get("/", include_in_schema=False)
def serve_ui():
    """Serve the main chat UI at the root URL."""
    return FileResponse(os.path.join(_FRONTEND_DIR, "index.html"))


@app.get("/health")
def root():
    """Simple health check -- confirms the server is up and reachable."""
    return {"status": "ok", "service": "ai-support-chatbot-api"}
