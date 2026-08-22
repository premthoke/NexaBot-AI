"""chat.py — full pipeline: preprocess -> classify intent -> extract entities -> FAQ lookup -> Gemini rewrite -> save history."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.database.models import ChatHistory
from backend.schemas.schemas import ChatRequest, ChatResponse
from backend.nlp.models.intent_classifier import predict_intent
from backend.nlp.ner import extract_entities
from backend.services.business_logic import get_answer
from backend.services.gemini_services import rewrite_answer

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
def chat(payload: ChatRequest, db: Session = Depends(get_db)):
    intent, confidence = predict_intent(payload.message)
    entities = extract_entities(payload.message)
    faq_answer, resolved_intent = get_answer(intent, confidence)
    reply_text = rewrite_answer(payload.message, faq_answer)

    history_row = ChatHistory(
        user_id=None,
        session_id=payload.session_id,
        user_message=payload.message,
        detected_intent=resolved_intent,
        bot_reply=reply_text,
    )
    db.add(history_row)
    db.commit()

    return ChatResponse(
        reply=reply_text,
        detected_intent=resolved_intent,
        extracted_entities=entities or None,
        confidence=round(confidence, 4),
    )
