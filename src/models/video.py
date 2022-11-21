from __future__ import annotations

import json
from src.models.caption import Caption
from src.common.utils import sanitize_text


class Video:
    def __init__(self, id, transcript) -> Video:
        """
        Initialize the video object
        :param id: video id
        :param transcript: dict transcript
        """
        self.id = id
        self.transcript = transcript
        self.captions = []
        self.append_captions_to_video()

    def append_captions_to_video(self) -> None:
        """
        Append the captions to the video object
        """
        for caption in self.transcript:
            sanitized_text = sanitize_text(caption["text"])
            end = caption["start"] + caption["duration"]
            self.captions.append(
                Caption(caption["start"], end, caption["duration"], sanitized_text)
            )

    def get_video_json(self) -> str:
        """
        Get the video transcript in JSON format
        :return: JSON string
        """
        json_video = json.dumps(self.__dict__, default=lambda o: o.__dict__)
        return json_video
