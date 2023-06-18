"""empty message

Revision ID: c702a173f3b9
Revises: 
Create Date: 2023-03-08 16:23:49.785570

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c702a173f3b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('flag', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('instructor')
    with op.batch_alter_table('student_degree', schema=None) as batch_op:
        batch_op.drop_index('student_id')

    op.drop_table('student_degree')
    op.drop_table('register_change')
    with op.batch_alter_table('section', schema=None) as batch_op:
        batch_op.drop_index('sec_id_2')
        batch_op.drop_index('sec_id_3')

    op.drop_table('section')
    op.drop_table('official_document')
    op.drop_table('teaches')
    op.drop_table('scientific_project')
    op.drop_table('takes')
    op.drop_table('linfeng')
    op.drop_table('meeting')
    op.drop_table('work_plan')
    with op.batch_alter_table('comment_on_teaching', schema=None) as batch_op:
        batch_op.drop_index('course')

    op.drop_table('comment_on_teaching')
    op.drop_table('bill')
    op.drop_table('student_dorm')
    op.drop_table('time_slot')
    op.drop_table('teacher')
    op.drop_table('exam_place')
    op.drop_table('enrollment_plan')
    op.drop_table('administrator')
    op.drop_table('exam')
    op.drop_table('teacher_info')
    op.drop_table('instructor_paper')
    op.drop_table('classroom')
    op.drop_table('fixed_assets')
    op.drop_table('college')
    op.drop_table('course')
    op.drop_table('sectionwithtimeslot')
    op.drop_table('class_schedule')
    op.drop_table('fee')
    op.drop_table('duty')
    op.drop_table('department')
    op.drop_table('exam_score')
    op.drop_table('student')
    op.drop_table('profession')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profession',
    sa.Column('pID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.Column('department', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=True),
    sa.Column('introduce', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.PrimaryKeyConstraint('pID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('student',
    sa.Column('sID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('dept_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('tot_cred', mysql.INTEGER(), server_default=sa.text("'0'"), autoincrement=False, nullable=True),
    sa.Column('password', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=True),
    sa.Column('phone_number', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=12), nullable=True),
    sa.Column('home', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('enter', mysql.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['dept_name'], ['department.dept_name'], name='student_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('sID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('exam_score',
    sa.Column('sID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('course_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=False),
    sa.Column('credit', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('course_attribute', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=10), nullable=True),
    sa.Column('exam_type', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('score', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('sID', 'course_name'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('department',
    sa.Column('dept_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('building', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=True),
    sa.Column('budget', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('introduce', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.PrimaryKeyConstraint('dept_name'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('duty',
    sa.Column('tID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('duty', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=True),
    sa.ForeignKeyConstraint(['tID'], ['instructor.tID'], name='duty_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('tID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('fee',
    sa.Column('sID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('cost_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=False),
    sa.Column('cost', mysql.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('pay_date', mysql.DATETIME(fsp=6), nullable=True),
    sa.Column('cost_state', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.ForeignKeyConstraint(['sID'], ['student.sID'], name='fee_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('sID', 'cost_name'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('class_schedule',
    sa.Column('sID', mysql.VARCHAR(length=5), nullable=False),
    sa.Column('course_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=30), nullable=False),
    sa.Column('course_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('dept_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('credits', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('time', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('place', mysql.VARCHAR(length=255), nullable=False),
    sa.ForeignKeyConstraint(['dept_name'], ['department.dept_name'], name='class_schedule_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('course_id', 'sID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('sectionwithtimeslot',
    sa.Column('course_id', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=30), nullable=False),
    sa.Column('sec_id', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=8), nullable=False),
    sa.Column('semester', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=6), nullable=True),
    sa.Column('year', mysql.DECIMAL(precision=4, scale=0), nullable=True),
    sa.Column('time_slot_id', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=4), nullable=True),
    sa.ForeignKeyConstraint(['time_slot_id'], ['time_slot.time_slot_id'], name='sectionwithtimeslot_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('course',
    sa.Column('course_id', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('dept_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('credits', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('course_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('college',
    sa.Column('college', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('major', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('introduction', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('major'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('fixed_assets',
    sa.Column('dept_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('fixed_assets', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.ForeignKeyConstraint(['dept_name'], ['department.dept_name'], name='fixed_assets_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('dept_name'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('classroom',
    sa.Column('building', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('room_no', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('capacity', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('building', 'room_no'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('instructor_paper',
    sa.Column('tID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('paper', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.ForeignKeyConstraint(['tID'], ['instructor.tID'], name='instructor_paper_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('tID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('teacher_info',
    sa.Column('tID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('teacher_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=15), nullable=False),
    sa.Column('teacher_department', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=15), nullable=True),
    sa.Column('teacher_phone', mysql.CHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=11), nullable=True),
    sa.Column('teacher_Political_outlook', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=16), nullable=True),
    sa.Column('teacher_title', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=25), nullable=True),
    sa.Column('teacher_category', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=25), nullable=True),
    sa.Column('teacher_organization', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=25), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('tID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('exam',
    sa.Column('course_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=30), nullable=False),
    sa.Column('sec_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=8), nullable=False),
    sa.Column('semester', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=6), nullable=False),
    sa.Column('year', mysql.DECIMAL(precision=4, scale=0), nullable=False),
    sa.Column('exam_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=7), nullable=False),
    sa.Column('building', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('room_no', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time', mysql.DATETIME(), nullable=True),
    sa.Column('duration', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('exam_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('administrator',
    sa.Column('adminID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('password', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.Column('department', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.PrimaryKeyConstraint('adminID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('enrollment_plan',
    sa.Column('year', mysql.YEAR(), nullable=False),
    sa.Column('enrollment_plan', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.PrimaryKeyConstraint('year'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('exam_place',
    sa.Column('exam_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=7), nullable=False),
    sa.Column('building', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('room_no', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('exam_id', 'building', 'room_no'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('teacher',
    sa.Column('tID', mysql.VARCHAR(length=5), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('tID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('time_slot',
    sa.Column('time_slot_id', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=4), nullable=False),
    sa.Column('day', mysql.ENUM('M', 'TU', 'W', 'TH', 'F', 'SA', 'SU'), nullable=False),
    sa.Column('start_time', mysql.DATETIME(), nullable=False),
    sa.Column('end_time', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('time_slot_id', 'day', 'start_time'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB',
    mysql_row_format='COMPACT'
    )
    op.create_table('student_dorm',
    sa.Column('s_ID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('student_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('student_domitory', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.ForeignKeyConstraint(['s_ID'], ['student.sID'], name='student_dorm_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('s_ID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('bill',
    sa.Column('s_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=7), nullable=False),
    sa.Column('amount', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('place', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=15), nullable=False),
    sa.Column('time', mysql.DATETIME(), nullable=False),
    sa.Column('balance', mysql.DECIMAL(precision=5, scale=1), nullable=False),
    sa.ForeignKeyConstraint(['s_id'], ['student.sID'], name='bill_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('s_id', 'time'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('comment_on_teaching',
    sa.Column('course_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=30), nullable=True),
    sa.Column('index', mysql.INTEGER(display_width=4, unsigned=True, zerofill=True), autoincrement=True, nullable=False),
    sa.Column('tID', mysql.VARCHAR(length=5), nullable=False),
    sa.Column('score', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=3), nullable=False),
    sa.PrimaryKeyConstraint('index'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    with op.batch_alter_table('comment_on_teaching', schema=None) as batch_op:
        batch_op.create_index('course', ['course_id'], unique=False)

    op.create_table('work_plan',
    sa.Column('tID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('work_plan', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=False),
    sa.Column('work_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('className', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('tID', 'work_plan'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('meeting',
    sa.Column('meeting_title', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.Column('department', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=True),
    sa.PrimaryKeyConstraint('meeting_title'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('linfeng',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('takes',
    sa.Column('sID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('course_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('sec_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('semester', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('year', mysql.DECIMAL(precision=4, scale=0), nullable=False),
    sa.Column('grade', mysql.DOUBLE(asdecimal=True), server_default=sa.text("'0'"), nullable=True),
    sa.Column('teacher_ID', mysql.VARCHAR(length=5), nullable=False),
    sa.Column('course_evaluate', mysql.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['section.course_id'], name='takes_ibfk_2', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['sID'], ['student.sID'], name='takes_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['sec_id', 'semester'], ['section.sec_id', 'section.semester'], name='takes_ibfk_3', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['year'], ['section.year'], name='takes_ibfk_4', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('sID', 'course_id', 'sec_id', 'semester', 'year', 'teacher_ID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('scientific_project',
    sa.Column('project_ID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.Column('project_status', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.PrimaryKeyConstraint('project_ID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('teaches',
    sa.Column('tID', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=5), nullable=False),
    sa.Column('course_id', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=50), nullable=False),
    sa.Column('sec_id', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=50), nullable=False),
    sa.Column('semester', mysql.VARCHAR(charset='utf8', collation='utf8_general_ci', length=50), nullable=False),
    sa.Column('year', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('tID', 'course_id', 'sec_id', 'semester', 'year'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('official_document',
    sa.Column('adminID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('official_document', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.Column('completion_status', sa.BINARY(length=1), nullable=True),
    sa.ForeignKeyConstraint(['adminID'], ['administrator.adminID'], name='official_document_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('adminID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('section',
    sa.Column('course_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=30), nullable=False),
    sa.Column('sec_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=8), nullable=False),
    sa.Column('semester', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=6), nullable=False),
    sa.Column('year', mysql.DECIMAL(precision=4, scale=0), nullable=False),
    sa.Column('building', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('room_no', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('course_id', 'sec_id', 'semester', 'year'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    with op.batch_alter_table('section', schema=None) as batch_op:
        batch_op.create_index('sec_id_3', ['sec_id', 'semester'], unique=False)
        batch_op.create_index('sec_id_2', ['sec_id', 'semester', 'year'], unique=False)

    op.create_table('register_change',
    sa.Column('sID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('register_change', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True),
    sa.ForeignKeyConstraint(['sID'], ['student.sID'], name='register_change_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('sID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('student_degree',
    sa.Column('s_ID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('student_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('student_degree', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=True),
    sa.ForeignKeyConstraint(['s_ID'], ['student.sID'], name='student_degree_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('s_ID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    with op.batch_alter_table('student_degree', schema=None) as batch_op:
        batch_op.create_index('student_id', ['s_ID'], unique=False)

    op.create_table('instructor',
    sa.Column('tID', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=False),
    sa.Column('name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=20), nullable=False),
    sa.Column('dept_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=50), nullable=False),
    sa.Column('salary', mysql.DECIMAL(precision=8, scale=2), nullable=True),
    sa.Column('password', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=5), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=11), nullable=True),
    sa.Column('Political_outlook', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('category', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('organization', mysql.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['dept_name'], ['department.dept_name'], name='instructor_ibfk_1', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('tID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.drop_table('users')
    # ### end Alembic commands ###
