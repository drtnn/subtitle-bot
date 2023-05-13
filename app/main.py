from aiofiles import os
from aiogram import executor

from app.data.settings import settings
from app.utils.dispatcher import register_handlers
from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    if not await os.path.exists(settings.CACHE_DIR):
        await os.makedirs(settings.CACHE_DIR)
    if not await os.path.exists(settings.VIDEO_DIR):
        await os.makedirs(settings.VIDEO_DIR)
    if not await os.path.exists(settings.AUDIO_DIR):
        await os.makedirs(settings.AUDIO_DIR)
    if not await os.path.exists(settings.SUBTITLES_DIR):
        await os.makedirs(settings.SUBTITLES_DIR)
    if not await os.path.exists(settings.RESULT_DIR):
        await os.makedirs(settings.RESULT_DIR)


if __name__ == "__main__":
    register_handlers(dp)
    executor.start_polling(dp, on_startup=on_startup)
