"""add tables

Revision ID: 79ba76563409
Revises: 084da67885df
Create Date: 2018-08-15 11:21:10.813705

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '79ba76563409'
down_revision = '084da67885df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unique_key', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('ip', sa.String(length=40), nullable=False),
    sa.Column('start_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_action', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unique_key')
    )
    op.create_table('submitted',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sessions_id', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('answer_id', sa.Integer(), nullable=True),
    sa.Column('submit_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('modify_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['answer_id'], ['answers.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['sessions_id'], ['sessions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('users_unique_key_key', 'users', type_='unique')
    op.drop_column('users', 'unique_key')
    op.drop_column('users', 'last_action')
    op.drop_column('users', 'start_time')
    op.drop_column('users', 'ip')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('ip', sa.VARCHAR(length=40), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('start_time', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('last_action', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('unique_key', postgresql.UUID(), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_unique_key_key', 'users', ['unique_key'])
    op.drop_table('submitted')
    op.drop_table('sessions')
    # ### end Alembic commands ###