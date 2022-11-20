import json
import logging

from typing import Union
from youtube_transcript_api import TranscriptList
from src.common.settings import InfoMsgs, LanguageEnum
from src.models.video import Video

class Transcriber:
    def __init__(self):
        logging.basicConfig(format="%(asctime)s %(message)s")

    def check_manual_and_language(self, transcript_list: TranscriptList) -> Union[bool, TranscriptList]:
        """
        Check if the transcript is manual and if the language is English
        :param transcript_list: transcript list
        :return: tuple of boolean and transcript list
        """
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

    def sanitize_transcript_and_create_video(self, video_id: str, transcript_list: TranscriptList) -> Video:
        """
        Sanitize the transcript
        :param video_id: video id
        :param transcript_list: transcript list
        :return: video object
        """
        logging.info(InfoMsgs.sanitizing_video.format(video_id=video_id))

        found_manual, caption_dict = self.check_manual_and_language(transcript_list)

        if not caption_dict:
            logging.info(InfoMsgs.couldnt_find_caption.format(video_id=video_id))
            video = Video(0, False, None)
            json_video = json.dumps(video, default=lambda o: o.__dict__)
            return json_video

        video = Video(video_id, found_manual)
        video.append_captions_to_video(caption_dict)

        return video