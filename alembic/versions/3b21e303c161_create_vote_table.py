"""create vote table

Revision ID: 3b21e303c161
Revises: 2957bf8b9bdb
Create Date: 2021-11-30 20:01:01.036063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b21e303c161'
down_revision = '2957bf8b9bdb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                  sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", 
                         source_table="posts", 
                         referent_table="users",
                         local_cols=["owner_id"],
                         remote_cols=["id"],
                         ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
