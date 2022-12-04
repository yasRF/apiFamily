"""empty message

Revision ID: 1e047da1b2b4
Revises: d9ae5e646e6a
Create Date: 2022-12-03 13:37:27.032564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e047da1b2b4'
down_revision = 'd9ae5e646e6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('family_lastname_key', 'family', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('family_lastname_key', 'family', ['lastname'])
    # ### end Alembic commands ###