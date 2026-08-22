"""
models.py

Defines the database tables as SQLAlchemy ORM classes. Every class here
maps 1:1 to a table; every attribute maps to a column.

These classes inherit from `Base` (declared in database.py), which is how
SQLAlchemy knows to track them and can create their tables in one call
(see init_db.py).
"""

from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from backend.database.database import Base


class User(Base):
    """A registered user of the chatbot (Phase 4 login/registration)."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # One user can have many chat messages. `back_populates` links this
    # to ChatHistory.user below, so SQLAlchemy keeps both sides in sync.
    chat_history = relationship("ChatHistory", back_populates="user")


class FAQ(Base):
    """
    A single business FAQ entry. `intent` is the label your Phase 7
    classifier will predict -- business_logic.py (Phase 9) looks up the
    row here whose `intent` matches the predicted intent.
    """

    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    intent = Column(String(50), nullable=False, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    category = Column(String(50), nullable=True)


class ChatHistory(Base):
    """
    One row per chat exchange. `user_id` is nullable because we want to
    support anonymous/guest chatting (no login required) as well as
    logged-in users -- a common real-world chatbot requirement.
    """

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    session_id = Column(String(64), nullable=False, index=True)
    user_message = Column(Text, nullable=False)
    detected_intent = Column(String(50), nullable=True)
    bot_reply = Column(Text, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="chat_history")
