from sqlalchemy import Table, Column, Integer, ForeignKey
from src.infra.database.connection import Base

task_tag = Table(
    'task_tag',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('task.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)