"""ner.py — entity extraction: spaCy for general entities + regex for custom business entities."""

import re
import spacy

try:
    _nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    _nlp = spacy.load("en_core_web_sm")

ORDER_ID_PATTERN = re.compile(r"\b(?:order\s*#?\s*)?#?(\d{4,10})\b", re.IGNORECASE)
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


def extract_entities(text: str) -> dict[str, str]:
    """Returns whatever custom + spaCy entities are found. Keys omitted if not present."""
    entities: dict[str, str] = {}

    email_match = EMAIL_PATTERN.search(text)
    if email_match:
        entities["email"] = email_match.group(0)

    order_match = ORDER_ID_PATTERN.search(text)
    if order_match and ("order" in text.lower() or "#" in text or "track" in text.lower() or "cancel" in text.lower()):
        entities["order_id"] = order_match.group(1)

    doc = _nlp(text)
    for ent in doc.ents:
        if ent.label_ in ("PRODUCT", "ORG"):
            entities.setdefault("product_name", ent.text)
        elif ent.label_ == "MONEY":
            entities.setdefault("amount", ent.text)

    return entities
