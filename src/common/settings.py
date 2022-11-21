import os


class InfoMsgs:
    user_already_in_db = "User [{name}, {email}] already exists in DB."
    user_added_to_db = "User [{name}, {email}] added to DB."
    transcribed_video = "Video with ID: {video_id} transcribed."
    getting_transcript = "Getting transcription for video with ID: {video_id}."
    getting_transcript_error = (
        "Error getting transcription for video with ID: {video_id}. Exception: {error}."
    )


class LanguageEnum:
    ENGLISH = "English"


class Config:
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "")

    MONGO_APP = os.environ.get("MONGO_APP", "")
    MONGO_LINK = os.environ.get("MONGO_LINK", "")
    MONGO_PASS = os.environ.get("MONGO_PASS", "")
