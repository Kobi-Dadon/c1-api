from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models import Base


class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    is_correct = Column(Boolean, nullable=False)
    text = Column(Text, nullable=False)

    question_id = Column(Integer, ForeignKey('questions.id'), nullable=True)
    questions = relationship('Questions', lazy='joined', foreign_keys=[question_id])
