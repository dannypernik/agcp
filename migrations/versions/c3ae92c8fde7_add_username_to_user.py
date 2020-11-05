"""add username to user

Revision ID: c3ae92c8fde7
Revises: 84f389422ff3
Create Date: 2020-10-24 17:12:38.590823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3ae92c8fde7'
down_revision = '84f389422ff3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###