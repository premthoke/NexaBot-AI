"""
gemini_services.py — uses Gemini ONLY to rephrase an already-retrieved FAQ
answer into a more natural, professional tone. Gemini never generates the
underlying policy/fact itself, and if it's unavailable, the raw FAQ answer
is still returned so the bot keeps working.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"

_model = None
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    _model = genai.GenerativeModel(MODEL_NAME)

PROMPT_TEMPLATE = """You are a customer support assistant. Rewrite the FAQ answer below in a
warm, professional, human tone in 2-3 sentences.

Rules:
- Do NOT add any new facts, policies, numbers, or promises not present in the FAQ answer.
- Do NOT change any numbers, deadlines, or policy details.
- Only rephrase for tone and clarity.

User's question: {user_message}
FAQ answer to rewrite: {faq_answer}

Rewritten answer:"""


def rewrite_answer(user_message: str, faq_answer: str) -> str:
    """Returns Gemini's rephrased answer, or the original FAQ answer if Gemini isn't configured/fails."""
    if _model is None:
        return faq_answer

    try:
        prompt = PROMPT_TEMPLATE.format(user_message=user_message, faq_answer=faq_answer)
        response = _model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.4,
                max_output_tokens=150,
            ),
        )
        text = (response.text or "").strip()
        return text if text else faq_answer
    except Exception:
        # Never let an LLM/network hiccup take down the chat endpoint.
        return faq_answer
