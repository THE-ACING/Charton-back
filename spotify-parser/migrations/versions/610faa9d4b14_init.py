"""init

Revision ID: 610faa9d4b14
Revises: 
Create Date: 2024-11-23 01:41:11.903869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '610faa9d4b14'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('spotify_id', sa.String(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_authors')),
    sa.UniqueConstraint('spotify_id', name=op.f('uq_authors_spotify_id'))
    )
    op.create_table('tracks',
    sa.Column('spotify_id', sa.String(), nullable=False),
    sa.Column('author_id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], name=op.f('fk_tracks_author_id_authors')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tracks')),
    sa.UniqueConstraint('spotify_id', name=op.f('uq_tracks_spotify_id'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tracks')
    op.drop_table('authors')
    # ### end Alembic commands ###
