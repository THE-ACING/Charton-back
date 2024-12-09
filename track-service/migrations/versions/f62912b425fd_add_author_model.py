"""add author model

Revision ID: f62912b425fd
Revises: 2647a792c5ba
Create Date: 2024-11-23 17:30:28.023645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f62912b425fd'
down_revision: Union[str, None] = '2647a792c5ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('genres', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_authors'))
    )
    op.add_column('tracks', sa.Column('author_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(op.f('fk_tracks_author_id_authors'), 'tracks', 'authors', ['author_id'], ['id'])
    op.drop_column('tracks', 'author')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracks', sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(op.f('fk_tracks_author_id_authors'), 'tracks', type_='foreignkey')
    op.drop_column('tracks', 'author_id')
    op.drop_table('authors')
    # ### end Alembic commands ###
