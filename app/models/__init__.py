from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker
from config.database import db_url

Base = declarative_base()
engine = create_engine(db_url())
Session = sessionmaker(bind=engine)


class Model(Base):
    __abstract__ = True

    def save(self):
        with Session.begin() as session:
            session.add(self)

    def update(self):
        mapped_values = {}
        pks = [col.name for col in inspect(type(self)).primary_key]

        filter_by = {}

        table_cols = inspect(type(self)).columns.keys()
        values = vars(self)

        for col in table_cols:
            if col in pks:
                filter_by[col] = values.get(col)
            else:
                mapped_values[col] = values.get(col)

        with Session.begin() as session:
            return session.query(type(self)) \
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
