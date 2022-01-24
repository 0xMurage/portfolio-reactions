from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config.database import db_url

Base = declarative_base()
engine = create_engine(db_url())
Session = sessionmaker(bind=engine)

from datetime import datetime


class Model(Base):
    __abstract__ = True

    def save(self):
        with Session.begin() as session:
            session.add(self)

    def update(self):
        mapped_values = {}
        pks = [pk.name for pk in self.__mapper__.primary_key]
        filter_by = {}

        obj = self.__dict__

        for field in obj.items():
            if field[0] in pks:
                filter_by[field[0]] = field[1]
            elif field[0] in self.__mapper__.columns:
                mapped_values[field[0]] = field[1]

        with Session.begin() as session:
            return session.query(self.__class__) \
                .filter_by(**filter_by) \
                .update(mapped_values)

    def delete(self):
        with Session.begin() as session:
            session.delete(self)

    @classmethod
    def all(cls, **kwargs):
        with Session() as session:
            return session.query(cls).filter_by(**kwargs).all()

    @classmethod
    def first(cls, **kwargs):
        with Session() as session:
            return session.query(cls).filter_by(**kwargs).first()

    @classmethod
    def first_or_fail(cls, **kwargs):
        with Session() as session:
            return session.query(cls).filter_by(**kwargs).one()

    @classmethod
    def first_or_none(cls, **kwargs):
        with Session() as session:
            return session.query(cls).filter_by(**kwargs).one_or_none()

    @classmethod
    def count(cls, **kwargs):
        with Session() as session:
            return session.query.filter_by(**kwargs).count()
