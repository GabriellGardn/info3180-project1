"""empty message

Revision ID: 661844321e18
Revises: 
Create Date: 2023-03-09 15:23:53.584681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '661844321e18'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property_profiles')
    # ### end Alembic commands ###
