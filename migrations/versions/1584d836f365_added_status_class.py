"""added status class

Revision ID: 1584d836f365
Revises: 6c916f94e943
Create Date: 2019-05-13 16:07:45.286462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1584d836f365'
down_revision = '6c916f94e943'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status',
    sa.Column('citizen_id', sa.String(length=12), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('status_category', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['citizen_id'], ['citizen.citizen_id'], ),
    sa.PrimaryKeyConstraint('status_id')
    )
    op.create_index(op.f('ix_status_timestamp'), 'status', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_status_timestamp'), table_name='status')
    op.drop_table('status')
    # ### end Alembic commands ###
