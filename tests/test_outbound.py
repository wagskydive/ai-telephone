from src.outbound import select_personalities, run_outbound, outbound_loop
from src.personalities import Personality


def test_select_personalities():
    pers = [Personality("a", "A", 1, 0.5, "t", "p"), Personality("b", "B", 2, 0.1, "t", "p")]
    r = iter([0.4, 0.2])
    selected = select_personalities(pers, rand=lambda: next(r))
    assert selected == [pers[0]]


def test_run_outbound():
    pers = [Personality("a", "A", 1, 0.9, "t", "p")]
    calls = []
    run_outbound(pers, originate=lambda ext: calls.append(ext), rand=lambda: 0.1)
    assert calls == [1]


def test_outbound_loop(monkeypatch):
    pers = [Personality("a", "A", 1, 0.9, "t", "p")]
    calls = []
    sleep_calls = 0

    def sleep(_):
        nonlocal sleep_calls
        sleep_calls += 1
        if sleep_calls > 1:
            raise KeyboardInterrupt

    monkeypatch.setattr("time.sleep", sleep)
    try:
        outbound_loop(
            pers,
            originate=lambda ext: calls.append(ext),
            interval=0,
            rand=lambda: 0.1,
        )
    except KeyboardInterrupt:
        pass
    assert calls == [1, 1]
