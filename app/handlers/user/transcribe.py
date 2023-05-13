import uuid

from aiogram.types import Message

from app.loader import bot
from app.utils.download_video import download_video
from app.utils.transcribe import transcribe


async def transcribe_video_note(message: Message):
    await message.answer("⏱️ Начался процесс транскрибирования...")
    file = await bot.get_file(message.video_note.file_id)
    request_id = uuid.uuid4()
    video_path = await download_video(request_id, file)
    result_path = transcribe(request_id, video_path)
    await message.answer_video_note(open(result_path, "rb"))


async def transcribe_video(message: Message):
    await message.answer("⏱️ Начался процесс транскрибирования...")
    file = await bot.get_file(message.video.file_id)
    request_id = uuid.uuid4()
    video_path = await download_video(request_id, file)
    result_path = transcribe(request_id, video_path)
    await message.answer_video(open(result_path, "rb"))
