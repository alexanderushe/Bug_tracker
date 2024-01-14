"""Edit comments table

Revision ID: 684748a651f4
Revises: 3459893a295e
Create Date: 2023-12-11 16:15:32.322890

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '684748a651f4'
down_revision = '3459893a295e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('text', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ticket_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], name='comments_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comments_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###