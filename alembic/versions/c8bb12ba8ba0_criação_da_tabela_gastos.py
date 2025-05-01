"""criação da tabela gastos

Revision ID: c8bb12ba8ba0
Revises: c88ca4d772ce
Create Date: 2025-05-01 01:20:03.696682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8bb12ba8ba0'
down_revision: Union[str, None] = 'c88ca4d772ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'gastos',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('data', sa.Date(), nullable=False),
        sa.Column('categoria', sa.String(), nullable=False),
        sa.Column('descricao', sa.String(), nullable=True),
        sa.Column('valor', sa.Float(), nullable=False),
        sa.Column('tipo', sa.String(), nullable=False),
        sa.Column('forma_pagamento', sa.String(), nullable=True),
    )

def downgrade():
    op.drop_table('gastos')