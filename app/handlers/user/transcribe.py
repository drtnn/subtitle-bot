import uuid
from typing import Callable

from aiogram.types import Message, File

from app.loader import bot
from app.utils.cache import delete_cache
from app.utils.download_video import download_video
from app.utils.transcribe import transcribe


async def transcribe_video_note(message: Message):
    await transcribe_content(message, message.video_note.file_id, message.answer_video_note)


async def transcribe_video(message: Message):
    await transcribe_content(message, message.video.file_id, message.answer_video)


async def transcribe_content(message: Message, file: File, send_video_func: Callable):
    await message.answer("⏱️ Начался процесс транскрибирования...")
    file = await bot.get_file(file)
    request_id = uuid.uuid4()
    video_path = await download_video(request_id, file)
    result_path = transcribe(request_id, video_path)
    await send_video_func(open(result_path, "rb"))
    await delete_cache(request_id)
