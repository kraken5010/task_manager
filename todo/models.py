from sqlalchemy import Column, String, Integer, Boolean

from database.base import Base, engine


class ToDo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
