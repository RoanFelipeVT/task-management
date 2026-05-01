from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.infra.database.connection import Base
from .associations import task_tag

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    #Relacionamentos
    user = relationship('User', back_populates='tasks')
    tags = relationship('Tag', secondary=task_tag, back_populates='tasks')