from sqlalchemy import Column, String, Integer, Boolean, text, TIMESTAMP
from app.models import Model


class Reaction(Model):
    __tablename__ = 'reactions'

    id = Column(Integer, autoincrement=True, primary_key=True)
    device_id = Column('device_id', String(255), nullable=False)
    project_id = Column(String(255), nullable=False)
    reaction = Column(Boolean, nullable=False, server_default=text('1'))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'))
    deleted_at = Column('deleted_at', TIMESTAMP, nullable=True)
