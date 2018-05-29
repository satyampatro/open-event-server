"""empty message

Revision ID: a3cf002f4da8
Revises: 194a5a2a44ef
Create Date: 2018-05-29 16:02:03.791772

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'a3cf002f4da8'
down_revision = '194a5a2a44ef'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stripe_authorizations', sa.Column('stripe_auth_code', sa.String(), nullable=True))
    op.drop_column('stripe_authorizations', 'stripe_email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stripe_authorizations', sa.Column('stripe_email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('stripe_authorizations', 'stripe_auth_code')
    # ### end Alembic commands ###