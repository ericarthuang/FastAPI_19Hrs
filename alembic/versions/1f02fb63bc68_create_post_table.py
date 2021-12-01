"""create post table

Revision ID: 1f02fb63bc68
Revises: 
Create Date: 2021-11-30 19:00:23.145130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f02fb63bc68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
