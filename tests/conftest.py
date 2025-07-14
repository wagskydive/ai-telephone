import sys
from pathlib import Path
import types

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

for name in ("sounddevice", "webrtcvad", "requests"):
    if name not in sys.modules:
        module = types.ModuleType(name)
        if name == "requests":
            def dummy_post(*a, **kw):
                raise RuntimeError("dummy")
            module.post = dummy_post
        elif name == "sounddevice":
            class DummyStream:
                def __init__(self, *a, **kw):
                    pass
                def __enter__(self):
                    return self
                def __exit__(self, exc_type, exc, tb):
                    pass
                def read(self, *a, **kw):
                    return b""
            module.RawInputStream = DummyStream
        elif name == "webrtcvad":
            class DummyVad:
                def is_speech(self, *a, **kw):
                    return False
            module.Vad = DummyVad
        sys.modules[name] = module
