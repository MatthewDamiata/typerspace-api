from src.api.youtube import get_transcript_from_api
from youtube_transcript_api import TranscriptsDisabled


def test_get_transcript_happy(
    monkeypatch, generate_random_youtube_id, mock_get_transcript
):

    monkeypatch.setattr(
        "src.api.youtube.YouTubeTranscriptApi.get_transcript", mock_get_transcript
    )
    video_id = generate_random_youtube_id()

    response = get_transcript_from_api(video_id)
    first_caption = response[0]

    assert type(response) == list
    assert type(first_caption) == dict
    assert "start" in first_caption
    assert "text" in first_caption
    assert "duration" in first_caption


def test_get_transcript_error(
    monkeypatch, generate_random_youtube_id, mock_raise_transcripts_disabled
):
    monkeypatch.setattr(
        "src.api.youtube.YouTubeTranscriptApi.get_transcript",
        mock_raise_transcripts_disabled,
    )

    video_id = generate_random_youtube_id()

    try:
        get_transcript_from_api(video_id)
    except Exception as error:
        assert type(error) == TranscriptsDisabled
