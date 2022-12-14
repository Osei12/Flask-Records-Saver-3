"""empty message

Revision ID: dcd0bd2e831d
Revises: 2d7821e9d0d5
Create Date: 2022-10-21 10:32:59.157769

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dcd0bd2e831d'
down_revision = '2d7821e9d0d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('member_records', 'gps_address')
    op.drop_column('member_records', 'when_did_you_join_the_church')
    op.drop_column('member_records', 'email')
    op.drop_column('member_records', 'name_of_basic_sch')
    op.drop_column('member_records', 'inst_of_work')
    op.drop_column('member_records', 'mortality_mother')
    op.drop_column('member_records', 'hometown')
    op.drop_column('member_records', 'active_in_department')
    op.drop_column('member_records', 'emergency_contact_name')
    op.drop_column('member_records', 'level_of_education')
    op.drop_column('member_records', 'emergency_contact_no')
    op.drop_column('member_records', 'name_of_tertiary_sch')
    op.drop_column('member_records', 'region')
    op.drop_column('member_records', 'baptized_by_immersion')
    op.drop_column('member_records', 'courses_offered')
    op.drop_column('member_records', 'house_no')
    op.drop_column('member_records', 'mortality_father')
    op.drop_column('member_records', 'phone')
    op.drop_column('member_records', 'place_of_residence')
    op.drop_column('member_records', 'prominent_landmark')
    op.drop_column('member_records', 'post_grad_courses_offered')
    op.drop_column('member_records', 'marital_status')
    op.drop_column('member_records', 'name_of_2nd_cycle_sch')
    op.drop_column('member_records', 'fathers_name')
    op.drop_column('member_records', 'relations')
    op.drop_column('member_records', 'mothers_name')
    op.drop_column('member_records', 'no_of_children')
    op.drop_column('member_records', 'when_were_you_born_again')
    op.drop_column('member_records', 'baptized_by_holy_spirit')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member_records', sa.Column('baptized_by_holy_spirit', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('when_were_you_born_again', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('no_of_children', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('mothers_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('relations', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('fathers_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('name_of_2nd_cycle_sch', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('marital_status', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('post_grad_courses_offered', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('prominent_landmark', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('place_of_residence', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('mortality_father', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('house_no', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('courses_offered', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('baptized_by_immersion', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('region', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('name_of_tertiary_sch', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('emergency_contact_no', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('level_of_education', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('emergency_contact_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('active_in_department', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('hometown', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('mortality_mother', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('inst_of_work', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('name_of_basic_sch', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('when_did_you_join_the_church', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('member_records', sa.Column('gps_address', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
