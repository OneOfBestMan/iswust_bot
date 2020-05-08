"""init

Revision ID: 9c4d517c3014
Revises:
Create Date: 2020-05-08 12:02:57.141037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9c4d517c3014"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "chat_records",
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("self_id", sa.Integer(), nullable=True),
        sa.Column("ctx_id", sa.String(length=64), nullable=True),
        sa.Column("msg", sa.String(), nullable=True),
        sa.Column("out", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "course",
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("term", sa.String(length=32), nullable=True),
        sa.Column("course_name", sa.String(length=64), nullable=True),
        sa.Column("course_idx", sa.String(length=16), nullable=True),
        sa.Column("time4class", sa.String(length=64), nullable=True),
        sa.Column("teacher_name", sa.String(length=32), nullable=True),
        sa.Column("location", sa.String(length=64), nullable=True),
        sa.Column("course_table", sa.LargeBinary(), nullable=True),
        sa.Column("start_week", sa.Integer(), nullable=True),
        sa.Column("end_week", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "sub_content",
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.Column("link", sa.String(length=128), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=True),
        sa.Column("content", sa.LargeBinary(), nullable=True),
        sa.PrimaryKeyConstraint("link"),
    )
    op.create_table(
        "user",
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.Column("qq", sa.String(length=16), nullable=False),
        sa.Column("student_id", sa.String(length=32), nullable=True),
        sa.Column("password", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=True),
        sa.Column("class", sa.String(length=16), nullable=True),
        sa.Column("cookies", sa.LargeBinary(), nullable=True),
        sa.PrimaryKeyConstraint("qq"),
        sa.UniqueConstraint("student_id"),
    )
    op.create_table(
        "course_student",
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.Column("student_id", sa.String(length=32), nullable=False),
        sa.Column("course_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["course_id"], ["course.id"], onupdate="CASCADE", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["student_id"], ["user.student_id"], onupdate="CASCADE", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("student_id", "course_id"),
    )
    op.create_table(
        "score_credit_progress",
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.Column("student_id", sa.String(length=32), nullable=False),
        sa.Column("total", sa.Float(), nullable=True),
        sa.Column("required", sa.Float(), nullable=True),
        sa.Column("elective", sa.Float(), nullable=True),
        sa.Column("sport", sa.Float(), nullable=True),
        sa.Column("common", sa.Float(), nullable=True),
        sa.Column("degree", sa.Float(), nullable=True),
        sa.Column("average_gpa", sa.Float(), nullable=True),
        sa.Column("required_gpa", sa.Float(), nullable=True),
        sa.Column("degree_gpa", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(
            ["student_id"], ["user.student_id"], onupdate="CASCADE", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("student_id"),
    )
    op.create_table(
        "score_plan",
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.Column("student_id", sa.String(length=32), nullable=False),
        sa.Column("course_id", sa.String(length=16), nullable=False),
        sa.Column("term", sa.String(length=64), nullable=False),
        sa.Column("course_name", sa.String(length=64), nullable=True),
        sa.Column("property", sa.String(length=64), nullable=True),
        sa.Column("credit", sa.Float(), nullable=True),
        sa.Column("score", sa.String(length=16), nullable=True),
        sa.Column("make_up_score", sa.String(length=16), nullable=True),
        sa.Column("gpa", sa.Float(), nullable=True),
        sa.Column("season", sa.String(length=16), nullable=True),
        sa.ForeignKeyConstraint(
            ["student_id"], ["user.student_id"], onupdate="CASCADE", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("student_id", "course_id", "term"),
    )
    op.create_table(
        "sub_user",
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.Column("ctx_id", sa.String(length=64), nullable=False),
        sa.Column("link", sa.String(length=128), nullable=False),
        sa.Column("only_title", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["link"], ["sub_content.link"], onupdate="CASCADE", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("ctx_id", "link"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sub_user")
    op.drop_table("score_plan")
    op.drop_table("score_credit_progress")
    op.drop_table("course_student")
    op.drop_table("user")
    op.drop_table("sub_content")
    op.drop_table("course")
    op.drop_table("chat_records")
    # ### end Alembic commands ###
