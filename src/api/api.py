import logging

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptList
from src.common.settings import InfoMsgs


def get_transcript_list(video_id: str) -> TranscriptList:
    """
    Get the transcript list for a video using YoutubeTranscriptApi
    :param video_id: video id
    :return: transcript list
    """
    try:
        logging.info(InfoMsgs.getting_transcription_list.format(video_id=video_id))
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    except Exception as e:
        logging.error(InfoMsgs.transcribed_video_error.format(video_id=video_id, error=e))
        return {"error": e}
    return transcript_list