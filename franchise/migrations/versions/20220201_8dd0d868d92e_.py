"""empty message

Revision ID: 8dd0d868d92e
Revises: 33a2dc242c12
Create Date: 2022-02-01 19:23:31.420641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dd0d868d92e'
down_revision = '33a2dc242c12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('coaches', 'team_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('teams', 'stadium_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('teams', 'admin_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teams', 'admin_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('teams', 'stadium_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('coaches', 'team_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###