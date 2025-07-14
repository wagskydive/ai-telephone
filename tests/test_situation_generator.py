from src.situation_generator import generate_situation
from unittest import mock


def test_generate_situation():
    with mock.patch('requests.post') as post:
        post.return_value.status_code = 200
        post.return_value.json.return_value = {'situation': 'test'}
        post.return_value.raise_for_status = lambda: None

        result = generate_situation('http://server', 'cap', ['m1'], 'prompt')

        post.assert_called_once_with(
            'http://server/generate-situation',
            json={'character_id': 'cap', 'memory_snippets': ['m1'], 'personality_prompt': 'prompt'}
        )
        assert result == 'test'
