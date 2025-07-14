def test_bootstrap_script_contents():
    text = open('bootstrap.sh').read()
    assert 'git clone' in text
    assert 'bash install.sh' in text

