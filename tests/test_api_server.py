from src.api_server import create_app
import io


def test_process_audio():
    app = create_app()
    client = app.test_client()
    response = client.post('/process-audio', data={'audio_file': (io.BytesIO(b'data'), 'in.wav')})
    assert response.status_code == 200
    assert response.data == b'data'


def test_generate_situation():
    app = create_app()
    client = app.test_client()
    response = client.post('/generate-situation', json={'character_id': 'cap'})
    assert response.status_code == 200
    assert response.get_json()['situation'] == 'situation for cap'
