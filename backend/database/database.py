"""
database.py

Sets up the connection to our SQLite database using SQLAlchemy.

Key concepts:
- Engine: the low-level object that manages the actual connection to the
  database file on disk.
- SessionLocal: a factory that creates new "session" objects. A session is
  like a workspace/transaction -- you use it to query and save data, then
  commit or roll back changes.
- Base: the parent class all our ORM models (models.py) inherit from. It
  keeps track of every table definition so we can create them all at once.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite connection string. "sqlite:///./chatbot.db" means:
# use SQLite, store the database file as chatbot.db in the current directory.
DATABASE_URL = "sqlite:///./chatbot.db"

# connect_args is SQLite-specific: by default SQLite only allows one thread
# to use a connection. FastAPI can handle requests across threads, so we
# disable that check here. (This is a well-known SQLite + FastAPI setting.)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Each instance of SessionLocal() will be a new database session.
# autocommit=False: we explicitly control when changes are saved (session.commit()).
# autoflush=False: SQLAlchemy won't auto-sync pending changes before every query.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that our models.py table classes inherit from.
Base = declarative_base()


def get_db():
    """
    Dependency function used by FastAPI (Phase 5) to provide a database
    session to each request, and guarantee it's closed afterward -- even
    if an error occurs. This "yield" pattern is a generator: FastAPI calls
    this, uses the session, then resumes after 'yield' to close it.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()