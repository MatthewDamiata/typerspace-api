import logging

from youtube_transcript_api import YouTubeTranscriptApi
from src.common.settings import InfoMsgs


def get_transcript(video_id: str) -> dict:
    """
    Get the transcript for a video using YoutubeTranscriptApi
    :param video_id: video id
    :return: transcript
    """
    try:
        logging.info(InfoMsgs.getting_transcript.format(video_id=video_id))
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=["en", "en-GB"]
        )
        return transcript
    except Exception as error:
        logging.error(
            InfoMsgs.getting_transcript_error.format(video_id=video_id, error=error)
        )
        return None
