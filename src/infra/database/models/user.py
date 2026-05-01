from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from src.infra.database.connection import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    cellphone = Column(String(20), nullable=True)
    photo = Column(String(255), nullable=True)

    # Relacionamentos
    tasks = relationship('Task', back_populates='user')
    tags = relationship('Tag', back_populates='user')