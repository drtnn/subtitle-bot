import uuid
from os import path

from aiofiles import os

from app.data.settings import settings


async def delete_cache(request_id: uuid.UUID):
    await os.remove(path.join(settings.VIDEO_DIR, f"{request_id}.mp4"))
    await os.remove(path.join(settings.AUDIO_DIR, f"{request_id}.wav"))
    await os.remove(path.join(settings.SUBTITLES_DIR, f"{request_id}.srt"))
    await os.remove(path.join(settings.RESULT_DIR, f"{request_id}.mp4"))
