"""create posts table

Revision ID: 86c858e67318
Revises: 
Create Date: 2022-08-13 20:35:12.580600

"""
from contextlib import nullcontext
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86c858e67318'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',        
        sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
        sa.Column('title',sa.String(),nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
