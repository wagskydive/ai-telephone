def test_vast_deploy_script():
    text = open('vast_deploy.sh').read()
    assert 'git clone' in text
    assert 'python -m src.api_server' in text
