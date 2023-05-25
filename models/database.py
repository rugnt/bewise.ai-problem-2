import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    token = Column(UUID(as_uuid=True), default=uuid.uuid4)
    audios = relationship('Audio')


class Audio(Base):
    __tablename__ = 'audios'

    audio_id = Column(Integer, primary_key=True)
    filename = Column(String(150), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))



