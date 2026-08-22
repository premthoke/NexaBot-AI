# AI Customer Support Chatbot (NLP + LLM)

Customer support chatbot combining classical NLP (TF-IDF + Logistic Regression
intent classification, spaCy NER) with Gemini for natural-language rewriting
of FAQ answers.

## Stack
Python · FastAPI · Streamlit · SQLite (SQLAlchemy) · spaCy · scikit-learn · Gemini API

## Setup

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Copy `.env.example` to `.env` and add your Gemini API key (optional — the
bot still works without it, just without the LLM rewrite step):

```bash
cp .env.example .env
```

## Initialize the database

```bash
python -m backend.database.init_db
```

## Train the intent classifier

```bash
python -m backend.nlp.models.train_intent_classifier
```

## Run it

Terminal 1 (backend):
```bash
uvicorn backend.main:app --reload
```

Terminal 2 (frontend):
```bash
streamlit run frontend/app.py
```

Backend docs: http://localhost:8000/docs
Frontend UI: http://localhost:8501

## Architecture

```
frontend/app.py (Streamlit)
        |
        v  HTTP
backend/main.py (FastAPI)
   |-- routers/auth.py   -> database/models.py (User)
   |-- routers/chat.py
        |-- nlp/preprocessing.py       (clean + lemmatize)
        |-- nlp/models/intent_classifier.py   (TF-IDF + LogisticRegression)
        |-- nlp/ner.py                 (spaCy + regex: order_id, email)
        |-- services/business_logic.py (intent -> FAQ answer, confidence threshold)
        |-- services/gemini_services.py (rewrite tone only, never invents facts)
        |-- database/models.py (ChatHistory)  <- every exchange is saved
```

## Data

- `data/intents_dataset.csv` — training examples for the intent classifier (8 intents:
  greeting, track_order, cancel_order, return_policy, product_inquiry, payment_issue,
  complaint, fallback)
- `data/faq_seed.csv` — the canned answer per intent that Gemini rewrites the tone of

## Notes

- Gemini is only ever used to *rephrase* an already-retrieved FAQ answer — it's
  explicitly instructed not to add facts, numbers, or policy details, and if
  `GEMINI_API_KEY` isn't set, the raw FAQ answer is returned unchanged.
- Confidence threshold for trusting the classifier is in `business_logic.py`
  (`CONFIDENCE_THRESHOLD`) — below it, the bot falls back rather than guessing.
- The included dataset is intentionally small (~85 rows) for demo purposes;
  expanding it per-intent will noticeably improve classification confidence
  and accuracy.
