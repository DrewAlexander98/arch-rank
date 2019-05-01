"""admins

Revision ID: ec0520f17139
Revises: 75da740a16e4
Create Date: 2019-05-01 20:49:57.180319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec0520f17139'
down_revision = '75da740a16e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.String(length=12), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('permission', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_index(op.f('ix_admin_name'), 'admin', ['name'], unique=False)
    op.create_index(op.f('ix_admin_permission'), 'admin', ['permission'], unique=False)
    op.add_column('citizen', sa.Column('permission', sa.String(length=20), nullable=True))
    op.create_index(op.f('ix_citizen_permission'), 'citizen', ['permission'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_citizen_permission'), table_name='citizen')
    op.drop_column('citizen', 'permission')
    op.drop_index(op.f('ix_admin_permission'), table_name='admin')
    op.drop_index(op.f('ix_admin_name'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###
