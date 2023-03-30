import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import settings

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'database', 'DB')
print(db_path)
if not os.path.exists(db_path):
    os.makedirs(db_path)

Base = declarative_base()

engine = create_engine(settings.db_url, connect_args={'check_same_thread': False}, echo=True)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()
