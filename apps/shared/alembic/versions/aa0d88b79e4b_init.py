"""init

Revision ID: aa0d88b79e4b
Revises:
Create Date: 2025-03-24 19:07:07.723360

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils.types.choice
from sqlalchemy_utils.types.choice import ChoiceType
from dashboard_app.app.models.watcher import ProtocolIDs


# revision identifiers, used by Alembic.
revision: str = "aa0d88b79e4b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "notification",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("wallet_id", sa.String(), nullable=False),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.Column(
            "ip_address",
            sqlalchemy_utils.types.ip_address.IPAddressType(length=50),
            nullable=True,
        ),
        sa.Column("health_ratio_level", sa.Float(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_notification_email"), "notification", ["email"], unique=False
    )

    op.add_column(
        "notification",
        sa.Column(
            "protocol_id", ChoiceType(ProtocolIDs, impl=sa.String()), nullable=False
        ),
    )
    op.create_table(
        "telegram_log",
        sa.Column("sent_at", sa.DateTime(), nullable=False),
        sa.Column("notification_data_id", sa.UUID(), nullable=False),
        sa.Column("is_succesfully", sa.Boolean(), nullable=False),
        sa.Column("message", sa.String(), server_default="", nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["notification_data_id"],
            ["notification.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("telegram_log")
    op.drop_index(op.f("ix_notification_email"), table_name="notification")
    op.drop_table("notification")
    # ### end Alembic commands ###
