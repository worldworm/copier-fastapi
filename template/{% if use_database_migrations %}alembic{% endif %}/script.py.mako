"""
Message: ${message}
Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}.
"""
# pylint: disable=invalid-name,no-member,unused-import,unnecessary-pass

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel

from alembic import op
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade the database."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade the database."""
    ${downgrades if downgrades else "pass"}
