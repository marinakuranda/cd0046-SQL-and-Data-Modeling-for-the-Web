"""empty message

Revision ID: 13890feec639
Revises: 68b0f1b51a9b
Create Date: 2023-12-17 18:23:43.887172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13890feec639'
down_revision = '68b0f1b51a9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.drop_column('genres')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
