"""empty message

Revision ID: 478c0005eabd
Revises: b6df793a4336
Create Date: 2024-04-19 09:20:51.478146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '478c0005eabd'
down_revision = 'b6df793a4336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('created', sa.String(length=120), nullable=True))
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('created')
        batch_op.drop_column('last_name')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
