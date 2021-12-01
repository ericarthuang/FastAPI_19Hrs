"""add new column to posts talbe

Revision ID: 1cfdd08a4a90
Revises: 1f02fb63bc68
Create Date: 2021-11-30 19:22:17.114584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cfdd08a4a90'
down_revision = '1f02fb63bc68'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                  sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
