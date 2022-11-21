import json

from src.main import read_transcript


def test_api_response(
    monkeypatch, generate_random_youtube_id, mock_get_transcript, validate_transcript
):
    video_id = generate_random_youtube_id()

    monkeypatch.setattr("src.main.get_transcript", mock_get_transcript)

    response = json.loads(read_transcript(video_id))

    assert response.get("id") == video_id
    assert response.get("transcript")
    transcript = response.get("transcript")

    validate_transcript(transcript)
