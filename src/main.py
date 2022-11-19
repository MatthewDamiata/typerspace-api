from fastapi import FastAPI
from src.translator import Transcriber

app = FastAPI()
transcriber = Transcriber()

@app.get("/video/{video_id}")
def read_transcript(video_id: str):
    return transcriber.get_video_json(video_id)
