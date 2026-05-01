from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.database.connection import Base
from .associations import task_tag

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'), nullable=False)

    #relacionamento
    user = relationship('User', back_populates='tags')
    tasks = relationship('Task', secondary=task_tag, back_populates='tags')