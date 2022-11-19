from fastapi import FastAPI
from src.translator import Transcriber

app = FastAPI()
transcriber = Transcriber()

@app.get("/video/{video_id}")
def read_transcript(video_id: str):
    """
    Returns the transcript of a video in JSON format
    :param video_id: the id of the video
    :return: the transcript of the video
    """
    return transcriber.get_video_json(video_id)
