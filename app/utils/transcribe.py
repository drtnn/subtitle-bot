import os
import uuid
from enum import Enum
from typing import Literal

import ffmpeg as ffmpeg
import whisper
from whisper.utils import write_srt

from app.data.settings import settings


class ModelType(Enum):
    value: str

    TINY_EN = "tiny.en"
    TINY = "tiny"
    BASE_EN = "base.en"
    BASE = "base"
    SMALL_EN = "small.en"
    SMALL = "small"
    MEDIUM_EN = "medium.en"
    MEDIUM = "medium"
    LARGE = "large"
    LARGE_V1 = "large-v1"
    LARGE_V2 = "large-v2"


def get_audio(request_id: uuid.UUID, path: str):
    output_path = os.path.join(settings.AUDIO_DIR, f"{request_id}.wav")

    ffmpeg.input(path).output(
        output_path,
        acodec="pcm_s16le", ac=1, ar="16k"
    ).run(quiet=True, overwrite_output=True)

    return output_path


def get_subtitles(request_id: uuid.UUID, model: whisper.model.Whisper, audio_path: str) -> str:
    subtitles = model.transcribe(audio_path)

    subtitles_path = os.path.join(settings.SUBTITLES_DIR, f"{request_id}.srt")

    with open(subtitles_path, "w", encoding="utf-8") as srt:
        write_srt(subtitles["segments"], file=srt, max_line_length=25)

    return subtitles_path


def transcribe(request_id: uuid.UUID, video_path: str, model_name: Literal[ModelType] = ModelType.SMALL):
    model = whisper.load_model(model_name.value)
    audio_path = get_audio(request_id, video_path)
    srt_path = get_subtitles(request_id, model, audio_path)

    result_path = os.path.join(settings.RESULT_DIR, f"{request_id}.mp4")

    video = ffmpeg.input(video_path)
    audio_path = video.audio

    ffmpeg.concat(
        video.filter('subtitles', srt_path,
                     force_style="OutlineColour=&H40000000,Fontname=Trebuchet MS,ScaleX=0.7,ScaleY=0.7,MarginV=15"),
        audio_path, v=1, a=1
    ).output(result_path).run(quiet=True, overwrite_output=True)

    return result_path
