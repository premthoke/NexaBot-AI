"""
init_db.py

Run this file directly (`python -m backend.database.init_db` from the
project root) to create the SQLite database file and all tables defined
in models.py.

Why a separate script instead of doing this inside main.py?
- Keeps "set up my database" a deliberate, explicit action you run once,
  not something that silently happens every time the API server starts.
- Makes it easy to re-run after adding a new model/column during
  development.
"""

from backend.database.database import Base, engine

# Importing models here (even though we don't use the names directly)
# is required: it's what makes SQLAlchemy aware these tables exist, so
# create_all() knows to create them. Without this import, Base.metadata
# would be empty.
from backend.database import models  # noqa: F401


def init_db() -> None:
    """Create all tables that don't already exist. Safe to run multiple times."""
    Base.metadata.create_all(bind=engine)
    print("Database initialized: chatbot.db (users, faqs, chat_history tables ready).")


if __name__ == "__main__":
    init_db()
