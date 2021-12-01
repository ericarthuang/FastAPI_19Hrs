"""complete the post table

Revision ID: 20f0af0dc370
Revises: 3b21e303c161
Create Date: 2021-11-30 20:21:09.516603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20f0af0dc370'
down_revision = '3b21e303c161'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                  sa.Column("published", 
                            sa.Boolean(), 
                            nullable=False, 
                            server_default="True"))
    op.add_column("posts",
                  sa.Column("create_at", 
                            sa.TIMESTAMP(timezone=True), 
                            nullable=False, 
                            server_default=sa.text("NOW()")))
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "create_at")
    pass
