"""add veriosn field for HashtackCollateralDebt

Revision ID: c65693d53658
Revises: fafbe0720bc8
Create Date: 2024-08-17 21:20:15.806069

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c65693d53658"
down_revision: Union[str, None] = "fafbe0720bc8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### Step 1: Add the new column as nullable ###
    op.add_column(
        "hashtack_collateral_debt", sa.Column("version", sa.Integer(), nullable=True)
    )

    # ### Step 2: Set default value (0) for existing records ###
    op.execute("UPDATE hashtack_collateral_debt SET version = 0")

    # ### Step 3: Alter the column to be non-nullable ###
    op.alter_column("hashtack_collateral_debt", "version", nullable=False)

    # ### Step 4: Create the index ###
    op.create_index(
        op.f("ix_hashtack_collateral_debt_version"),
        "hashtack_collateral_debt",
        ["version"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_hashtack_collateral_debt_version"),
        table_name="hashtack_collateral_debt",
    )
    op.drop_column("hashtack_collateral_debt", "version")
    # ### end Alembic commands ###
