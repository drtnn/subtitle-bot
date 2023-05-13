import os
import uuid

from aiogram.types import File

from app.data.settings import settings
from app.loader import bot


async def download_video(request_id: uuid.UUID, file: File) -> str:
    output_path = os.path.join(settings.VIDEO_DIR, f"{request_id}.mp4")
    await bot.download_file(file.file_path, output_path)
    return output_path
