"""User

Revision ID: cf95c3bff9a6
Revises: 4b217398aa2e
Create Date: 2023-05-12 10:10:25.029911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf95c3bff9a6'
down_revision = '4b217398aa2e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('dob', sa.String(), nullable=False))
    op.drop_column('users', 'd_o_b')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('d_o_b', sa.DATE(), autoincrement=False, nullable=False))
    op.drop_column('users', 'dob')
    # ### end Alembic commands ###
