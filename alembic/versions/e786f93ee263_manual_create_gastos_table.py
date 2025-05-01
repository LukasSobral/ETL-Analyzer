"""manual: create gastos table

Revision ID: e786f93ee263
Revises: c8bb12ba8ba0
Create Date: 2025-05-01 01:22:50.349445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e786f93ee263'
down_revision: Union[str, None] = 'c8bb12ba8ba0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
