"""create weather_table

Revision ID: 490a7d10f749
Revises: cd391ca19acf
Create Date: 2022-02-08 21:20:40.545144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '490a7d10f749'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'weather',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('city', sa.String(20), nullable=False),
        sa.Column('year', sa.Integer),
        sa.Column('month', sa.String(10)),
        sa.Column('temperature', sa.Float(10)),
    )


def downgrade():
    op.drop_table('weather')
