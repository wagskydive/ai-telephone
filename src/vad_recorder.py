"""Voice Activity Detector-based recorder."""
from pathlib import Path


def record_until_silence(output_path: Path) -> None:
    """Record audio until silence is detected.

    Parameters
    ----------
    output_path: Path
        Destination for the recorded WAV file.
    """
    # TODO: implement VAD loop
    pass
