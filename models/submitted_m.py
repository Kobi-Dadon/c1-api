from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from models import Base


class Submitted(Base):
    __tablename__ = 'submitted'
    id = Column(Integer, primary_key=True)
    sessions_id = Column(Integer, ForeignKey('sessions.id'), nullable=True)
    sessions = relationship('Sessions', uselist=False, lazy='joined', foreign_keys=[sessions_id])
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=True)
    questions = relationship('Questions', uselist=False, lazy='joined', foreign_keys=[question_id])
    answer_id = Column(Integer, ForeignKey('answers.id'), nullable=True)
    answer = relationship('Answers', uselist=False, lazy='joined', foreign_keys=[answer_id])
    submit_time = Column(DateTime, nullable=False, server_default=func.now(), default=func.now())
    modify_time = Column(DateTime, nullable=False, server_default=func.now(), default=func.now(),
                         server_onupdate=func.now(), onupdate=func.now())

    def __init__(self, **kwargs):
        self.sessions_id = kwargs.get('sessions_id')
        self.question_id = kwargs.get('question_id')
        self.answer_id = kwargs.get('answer_id')
