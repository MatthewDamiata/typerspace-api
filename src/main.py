from fastapi import FastAPI
from src.models.translator import Transcriber
from src.api.api import get_transcript_list


app = FastAPI()
transcriber = Transcriber()

@app.get("/video/{video_id}")
def read_transcript(video_id: str):
    """
    Returns the transcript of a video in JSON format
    :param video_id: the id of the video
    :return: the transcript of the video
    """
    transcript_list = get_transcript_list(video_id)
    video = transcriber.sanitize_transcript_and_create_video(video_id, transcript_list)
    video_json = video.get_video_json()

    return video_json
