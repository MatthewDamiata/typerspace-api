import json
import logging

from src.settings import InfoMsgs, LanguageEnum
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptList

class Video:
    def __init__(self, id, manual):
        self.id = id
        self.manual = manual
        self.captions = []

class Caption:
    def __init__(self, start, end, duration, text):
        self.start = start
        self.end = end
        self.duration = duration
        self.text = text

class Transcriber:
    def __init__(self):
        logging.basicConfig(format="%(asctime)s %(message)s")

    def get_transcript_list(self, video_id: str):
        try:
            logging.info(InfoMsgs.getting_transcription_list.format(video_id=video_id))
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        except Exception as e:
            logging.error(InfoMsgs.transcribed_video_error.format(video_id=video_id, error=e))
            return {"error": e}
        return transcript_list

    def sanitize_text(self, text: str):
        return text.replace(chr(34), "").replace("\n", " ").replace(chr(160), " "),

    def append_captions_to_video(self, video: Video, caption_dict: TranscriptList):
        for caption in caption_dict:
            sanitized_text = self.sanitize_text(caption["text"])
            end = caption["start"] + caption["duration"]
            video.captions.append(
                Caption(caption["start"], end, caption["duration"], sanitized_text)
            )

    def check_manual_and_langauge(self, transcript_list: TranscriptList):
        found_manual = False
        caption_dict = None
        for transcript in transcript_list:
            if (
                not transcript.is_generated
                and transcript.language == LanguageEnum.ENGLISH
            ):
                caption_dict = transcript.fetch()
                found_manual = True
                break
            if LanguageEnum.ENGLISH in transcript.language:
                caption_dict = transcript.fetch()

        return found_manual, caption_dict

    def sanitize_transcript(self, video_id: str, transcript_list: TranscriptList):
        logging.info(InfoMsgs.sanitizing_video.format(video_id=video_id))

        found_manual, caption_dict = self.check_manual_and_langauge(transcript_list)

        if not caption_dict:
            logging.info(InfoMsgs.couldnt_find_caption.format(video_id=video_id))
            video = Video(0, False)
            json_video = json.dumps(video, default=lambda o: o.__dict__)
            return json_video

        video = Video(video_id, found_manual)
        self.append_captions_to_video(video, caption_dict)

        return video

    def get_video_json(self, video_id: str):
        transcript_list = self.get_transcript_list(video_id)

        video = self.sanitize_transcript(video_id, transcript_list)

        json_video = json.dumps(video, default=lambda o: o.__dict__)
        logging.info(InfoMsgs.transcribed_video.format(video_id=video.id))
        return json_video