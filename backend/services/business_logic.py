"""business_logic.py — maps a detected intent to a canned FAQ answer, with confidence fallback."""

import csv
import os

CONFIDENCE_THRESHOLD = 0.22

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_PATH = os.path.join(BASE_DIR, "..", "..", "data", "faq_seed.csv")

_faq_map: dict[str, dict] = {}


def _load_faqs() -> dict[str, dict]:
    global _faq_map
    if not _faq_map:
        with open(FAQ_PATH, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                _faq_map[row["intent"]] = row
    return _faq_map


def get_answer(intent: str, confidence: float) -> tuple[str, str]:
    """
    Returns (answer_text, resolved_intent).
    Below CONFIDENCE_THRESHOLD, we don't trust the prediction and fall back
    instead of risking a confidently-wrong answer.
    """
    faqs = _load_faqs()

    if confidence < CONFIDENCE_THRESHOLD or intent not in faqs:
        return faqs["fallback"]["answer"], "fallback"

    return faqs[intent]["answer"], intent
