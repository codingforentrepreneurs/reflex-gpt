"""empty message

Revision ID: 6d5fa536a4f3
Revises: 8d2e0763fc8c
Create Date: 2024-08-28 15:16:53.853333

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '6d5fa536a4f3'
down_revision: Union[str, None] = '8d2e0763fc8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
