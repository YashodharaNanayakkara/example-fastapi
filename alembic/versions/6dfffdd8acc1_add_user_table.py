"""add user table

Revision ID: 6dfffdd8acc1
Revises: ca3244ae6c8d
Create Date: 2026-08-24 13:43:01.929340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6dfffdd8acc1'
down_revision: Union[str, Sequence[str], None] = 'ca3244ae6c8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )         
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
