"""create user table

Revision ID: 2957bf8b9bdb
Revises: 1cfdd08a4a90
Create Date: 2021-11-30 19:32:45.332838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2957bf8b9bdb'
down_revision = '1cfdd08a4a90'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("create_at", 
                              sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text("NOW()"), 
                              nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade():
    op.drop_talbe("users")
    pass
