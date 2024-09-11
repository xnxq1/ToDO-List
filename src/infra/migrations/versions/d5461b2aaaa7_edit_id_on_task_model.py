"""Edit id on Task model

Revision ID: d5461b2aaaa7
Revises: 
Create Date: 2024-09-11 11:45:39.644195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5461b2aaaa7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Task',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('priority', sa.Enum('high', 'medium', 'low', name='priority'), nullable=False),
    sa.Column('status', sa.Enum('completed', 'uncompleted', name='status'), nullable=False),
    sa.CheckConstraint('length(title) <= 255', name='check_title_length'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Task')
    # ### end Alembic commands ###
