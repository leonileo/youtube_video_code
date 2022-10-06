"""empty message

Revision ID: fa2aee555e15
Revises: e8ce5286a9b6
Create Date: 2022-09-30 22:06:39.849156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa2aee555e15'
down_revision = 'e8ce5286a9b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_joined', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date_joined')
    # ### end Alembic commands ###