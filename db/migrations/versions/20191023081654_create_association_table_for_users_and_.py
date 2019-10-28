"""create association table for users and books

Revision ID: 292b6920f2ec
Revises: abc3e212530c
Create Date: 2019-10-23 08:16:54.546972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '292b6920f2ec'
down_revision = 'abc3e212530c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_books_id'), 'user_books', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_books_id'), table_name='user_books')
    op.drop_table('user_books')
    # ### end Alembic commands ###
