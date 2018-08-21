from sqlalchemy import Column, Integer, String, Text, DateTime, func, text, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from models import Base


class Sessions(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    unique_key = Column(UUID(as_uuid=True), unique=True, nullable=False)
    ip = Column(String(40), nullable=False)
    start_time = Column(DateTime, nullable=False, server_default=func.now(), default=func.now())
    last_action = Column(DateTime, nullable=False, server_default=func.now(), default=func.now(),
                           server_onupdate=func.now(), onupdate=func.now())
    is_done = Column(Boolean, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship('Users', uselist=False, lazy='joined', foreign_keys=[user_id])
    # submitted = relationship('Submitted', lazy='joined', cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        self.ip = kwargs.get('ip')
        self.unique_key = kwargs.get('unique_key')
        self.user_id = kwargs.get('user_id')
        self.is_done = kwargs.get('is_done')