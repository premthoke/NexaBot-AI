"""preprocessing.py — text cleaning/normalization used before classification and NER."""

import re
import string

import spacy

try:
    _nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    _nlp = spacy.load("en_core_web_sm")


def clean_text(text: str) -> str:
    """Lowercase, strip URLs/extra whitespace, remove punctuation (keep alphanumerics)."""
    text = text.lower().strip()
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str) -> list[str]:
    doc = _nlp(text)
    return [token.text for token in doc]


def lemmatize(text: str, remove_stopwords: bool = True) -> str:
    """Lowercase -> lemmatize -> optionally drop stopwords/punctuation. Used for ML input."""
    doc = _nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if not token.is_punct and not token.is_space
        and (not remove_stopwords or not token.is_stop)
    ]
    return " ".join(tokens)


def preprocess_for_classification(text: str) -> str:
    """Full pipeline used before feeding text into the TF-IDF vectorizer."""
    return lemmatize(clean_text(text), remove_stopwords=True)
