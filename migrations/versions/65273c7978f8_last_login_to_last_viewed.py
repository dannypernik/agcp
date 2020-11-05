"""last_login to last_viewed

Revision ID: 65273c7978f8
Revises: 3ab4dc3066ed
Create Date: 2020-10-26 00:06:04.471920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65273c7978f8'
down_revision = '3ab4dc3066ed'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('last_viewed')
    op.add_column('user', sa.Column('last_viewed', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_login', sa.DATETIME(), nullable=True))
    op.drop_column('user', 'last_viewed')
    # ### end Alembic commands ###