from aiogram.dispatcher import Dispatcher

from app.handlers.user.transcribe import transcribe_video_note, transcribe_video


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(transcribe_video_note, content_types=["video_note"])
    dp.register_message_handler(transcribe_video, content_types=["video"])
