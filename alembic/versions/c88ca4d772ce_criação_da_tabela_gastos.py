"""criação da tabela gastos

Revision ID: c88ca4d772ce
Revises: 
Create Date: 2025-05-01 01:12:30.614650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c88ca4d772ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'gastos',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('data', sa.Date(), nullable=False),
        sa.Column('categoria', sa.String(), nullable=False),
        sa.Column('descricao', sa.String()),
        sa.Column('valor', sa.Float(), nullable=False),
        sa.Column('tipo', sa.String(), nullable=False),
        sa.Column('forma_pagamento', sa.String())
    )

def downgrade():
    op.drop_table('gastos')