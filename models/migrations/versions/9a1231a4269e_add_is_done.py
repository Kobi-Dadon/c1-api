"""add_is_done

Revision ID: 9a1231a4269e
Revises: efc2f40f82bb
Create Date: 2018-08-20 22:27:40.834828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a1231a4269e'
down_revision = 'efc2f40f82bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('is_done', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sessions', 'is_done')
    # ### end Alembic commands ###
