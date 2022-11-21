from fastapi import FastAPI, HTTPException
from src.api.youtube_api import get_transcript
from src.models.video import Video

app = FastAPI()


@app.get("/video/{video_id}")
def read_transcript(video_id: str):
    """
    Returns the transcript of a video in JSON format
    :param video_id: the id of the video
    :return: the transcript of the video
    """
    transcript = get_transcript(video_id)
    if not transcript:
        raise HTTPException(status_code=404, detail="Video not found")

    video = Video(video_id, transcript)
    return video.get_video_json()
