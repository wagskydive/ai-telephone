from src.gui.app import create_app
import json


def test_get_personalities(tmp_path, monkeypatch):
    data_file = tmp_path / "p.json"
    data_file.write_text(json.dumps([{"id": "p", "enabled": True}]))
    monkeypatch.setattr('src.gui.app.PERSONALITIES_FILE', data_file)
    monkeypatch.setattr('src.gui.app.MEMORY_DIR', tmp_path)
    app = create_app()
    client = app.test_client()
    resp = client.get('/api/personalities')
    assert resp.get_json() == [{"id": "p", "enabled": True}]


def test_toggle_personality(tmp_path, monkeypatch):
    data_file = tmp_path / "p.json"
    data_file.write_text(json.dumps([{"id": "p", "enabled": True}]))
    monkeypatch.setattr('src.gui.app.PERSONALITIES_FILE', data_file)
    monkeypatch.setattr('src.gui.app.MEMORY_DIR', tmp_path)
    app = create_app()
    client = app.test_client()
    resp = client.post('/api/personalities/p/toggle')
    assert resp.status_code == 200
    assert json.loads(data_file.read_text())[0]['enabled'] is False


def test_get_logs(tmp_path, monkeypatch):
    person_file = tmp_path / 'pers.json'
    person_file.write_text('[]')
    log_dir = tmp_path / 'logs'
    log_dir.mkdir()
    (log_dir / 'p.json').write_text('[{"summary": "hi"}]')
    monkeypatch.setattr('src.gui.app.PERSONALITIES_FILE', person_file)
    monkeypatch.setattr('src.gui.app.MEMORY_DIR', log_dir)
    app = create_app()
    client = app.test_client()
    resp = client.get('/api/logs/p')
    assert resp.get_json() == [{"summary": "hi"}]
