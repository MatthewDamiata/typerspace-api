import json

from youtube_transcript_api import TranscriptList
from src.models.caption import Caption
from src.common.utils import sanitize_text


class Video:
    def __init__(self, id, manual):
        """
        Initialize the video object
        :param id: video id
        :param manual: manual transcript
        """
        self.id = id
        self.manual = manual
        self.captions = []

    def append_captions_to_video(self, caption_dict: TranscriptList) -> None:
        """
        Append the captions to the video object
        :param video: video object
        :param caption_dict: dictionary of captions
        """
        for caption in caption_dict:
            sanitized_text = sanitize_text(caption["text"])
            end = caption["start"] + caption["duration"]
            self.captions.append(
                Caption(caption["start"], end, caption["duration"], sanitized_text)
            )

    def get_video_json(self) -> str:
        """
        Get the video transcript in JSON format
        :param video_id: video id
        :return: video transcript in JSON format
        """
        json_video = json.dumps(self.__dict__, default=lambda o: o.__dict__)
        return json_video
