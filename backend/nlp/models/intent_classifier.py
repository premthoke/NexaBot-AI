"""intent_classifier.py — loads the trained pipeline and exposes predict_intent()."""

import os
import joblib

from backend.nlp.preprocessing import preprocess_for_classification

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "intent_model.pkl")

_model = None


def _get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_intent(text: str) -> tuple[str, float]:
    """Returns (predicted_intent, confidence) where confidence is the top class probability."""
    model = _get_model()
    processed = preprocess_for_classification(text)
    probs = model.predict_proba([processed])[0]
    classes = model.classes_
    best_idx = probs.argmax()
    return classes[best_idx], float(probs[best_idx])
