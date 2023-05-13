import os
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str

    ADMINS: List[int]

    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    CACHE_DIR: str = os.path.join(BASE_DIR, "cache")
    VIDEO_DIR: str = os.path.join(CACHE_DIR, "videos")
    AUDIO_DIR: str = os.path.join(CACHE_DIR, "audios")
    SUBTITLES_DIR: str = os.path.join(CACHE_DIR, "subtitles")
    RESULT_DIR: str = os.path.join(CACHE_DIR, "result")

    class Config:
        case_sensitive = True


settings = Settings()
