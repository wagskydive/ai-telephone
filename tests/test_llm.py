from unittest import mock

from src import llm


def test_generate_response():
    with mock.patch('requests.post') as post:
        post.return_value.status_code = 200
        post.return_value.json.return_value = {'response': 'ok'}
        post.return_value.raise_for_status = lambda: None

        result = llm.generate_response('hi', 'prompt', url='http://x')

        post.assert_called_once_with('http://x/generate', json={'text': 'hi', 'prompt': 'prompt'})
        assert result == 'ok'
