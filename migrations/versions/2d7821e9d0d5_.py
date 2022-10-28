"""empty message

Revision ID: 2d7821e9d0d5
Revises: 
Create Date: 2022-10-21 10:29:29.400384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d7821e9d0d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('member_records', 'profile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member_records', sa.Column('profile', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
