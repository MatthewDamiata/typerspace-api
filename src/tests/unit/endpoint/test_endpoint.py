import json

from http import HTTPStatus
from src.main import read_transcript


def test_api_response(
    monkeypatch, generate_random_youtube_id, mock_get_transcript, validate_transcript
):
    monkeypatch.setattr("src.main.get_transcript_from_api", mock_get_transcript)

    video_id = generate_random_youtube_id()
    response = json.loads(read_transcript(video_id))

    assert response.get("id") == video_id
    assert response.get("transcript")

    transcript = response.get("transcript")
    validate_transcript(transcript)


def test_api_response_404(
    monkeypatch, generate_random_youtube_id, mock_get_404_transcript
):
    monkeypatch.setattr("src.main.get_transcript_from_api", mock_get_404_transcript)

    video_id = generate_random_youtube_id()

    try:
        read_transcript(video_id)
    except Exception as e:
        assert e.status_code == HTTPStatus.NOT_FOUND
        assert e.detail == "Video not found"
