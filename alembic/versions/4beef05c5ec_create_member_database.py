"""Create member database

Revision ID: 4beef05c5ec
Revises: 
Create Date: 2017-02-05 15:54:06.706073

"""

# revision identifiers, used by Alembic.
revision = '4beef05c5ec'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'member',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('global_nick', sa.Unicode(255)),
        sa.Column('local_nick', sa.Unicode(255)),
        sa.Column('points', sa.Integer),
        sa.Column('rank_id', sa.Integer),
    )

def downgrade():
    op.drop_table('member')
