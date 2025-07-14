def test_install_script_contents():
    text = open('install.sh').read()
    assert 'python3 -m venv' in text
    assert 'systemctl enable ai-telephone.service' in text


def test_service_file():
    text = open('systemd/ai-telephone.service').read()
    assert '-m src.api_server' in text
