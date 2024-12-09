from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PlaylistTrack
from app.repositories.base import BaseRepository


class PlaylistTrackRepository(BaseRepository[PlaylistTrack]):
    def __init__(self, session: AsyncSession):
        super().__init__(PlaylistTrack, session)
