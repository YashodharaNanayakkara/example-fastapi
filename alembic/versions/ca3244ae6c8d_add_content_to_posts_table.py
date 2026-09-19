"""add content to posts table

Revision ID: ca3244ae6c8d
Revises: 48f67ada18dd
Create Date: 2026-08-24 13:08:53.447285

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca3244ae6c8d'
down_revision: Union[str, Sequence[str], None] = '48f67ada18dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
