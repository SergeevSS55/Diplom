"""Add new column to users table

Revision ID: 8941d5aaae9c
Revises: 752a9ce92f4d
Create Date: 2024-12-16 20:17:01.726451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8941d5aaae9c'
down_revision: Union[str, None] = '752a9ce92f4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
