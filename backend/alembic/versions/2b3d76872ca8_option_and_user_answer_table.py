"""option and user answer table

Revision ID: 2b3d76872ca8
Revises: d8707b6317ee
Create Date: 2024-01-23 11:51:08.779203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b3d76872ca8'
down_revision = 'd8707b6317ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('option',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('friend_answer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('uid', sa.INTEGER(), nullable=True),
    sa.Column('qid', sa.INTEGER(), nullable=True),
    sa.Column('oid', sa.INTEGER(), nullable=True),
    sa.Column('fid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['fid'], ['user.id'], ),
    sa.ForeignKeyConstraint(['oid'], ['option.id'], ),
    sa.ForeignKeyConstraint(['qid'], ['question.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('question_option_association',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('qid', sa.INTEGER(), nullable=True),
    sa.Column('oid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['oid'], ['option.id'], ),
    sa.ForeignKeyConstraint(['qid'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user_answer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('uid', sa.INTEGER(), nullable=True),
    sa.Column('qid', sa.INTEGER(), nullable=True),
    sa.Column('oid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['oid'], ['option.id'], ),
    sa.ForeignKeyConstraint(['qid'], ['question.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'question', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question', type_='unique')
    op.drop_table('user_answer')
    op.drop_table('question_option_association')
    op.drop_table('friend_answer')
    op.drop_table('user')
    op.drop_table('option')
    # ### end Alembic commands ###
