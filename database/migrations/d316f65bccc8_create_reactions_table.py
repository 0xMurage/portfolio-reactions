"""create reactions table

Revision ID: d316f65bccc8
Revises: 
Create Date: 2022-01-22 17:03:10.325341

"""
from alembic import op
from sqlalchemy import Column, String, TIMESTAMP, Integer, SmallInteger, text, UniqueConstraint

# revision identifiers, used by Alembic.
revision = 'd316f65bccc8'
down_revision = None
branch_labels = None
depends_on = None

table_name = 'reactions'


def upgrade():
    op.create_table(table_name,
                    Column('id', Integer, autoincrement=True, primary_key=True),
                    Column('device_id', String(255), nullable=False),
                    Column('project_id', String(255), nullable=False),
                    Column('reaction', SmallInteger, nullable=False, server_default=text('1')),
                    Column('created_at', TIMESTAMP, nullable=False, server_default=text('now()')),
                    Column('deleted_at', TIMESTAMP, nullable=True),
                    UniqueConstraint('device_id', 'project_id', 'deleted_at','reaction',name='re')
                    )


def downgrade():
    op.drop_table(table_name)
