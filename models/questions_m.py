from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from models import Base
from models.answers_m import Answers


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    difficulty = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    answers = relationship('Answers', lazy='joined', cascade="all, delete-orphan")