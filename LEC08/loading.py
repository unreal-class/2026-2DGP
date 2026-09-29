"""Load and validate frame metadata without opening a graphics window."""
import json
from pathlib import Path

from sprite_model import Animation, Frame

ASSETS = Path(__file__).resolve().parent / "assets"


def load_animations():
    data = json.loads((ASSETS / "animations.json").read_text(encoding="utf-8"))
    stage = tuple(data["stage"])
    if len(stage) != 2 or min(stage) <= 0:
        raise ValueError("Invalid stage dimensions")
    animations = []
    for entry in data["animations"]:
        frames = tuple(Frame(**frame) for frame in entry["frames"])
        if not frames or entry["fps"] <= 0:
            raise ValueError("Each animation requires frames and positive FPS")
        for frame in frames:
            if min(frame.width, frame.height) <= 0 or min(frame.x, frame.y,
                    frame.offset_x, frame.offset_y) < 0:
                raise ValueError("Invalid frame rectangle")
            if (frame.offset_x + frame.width > stage[0]
                    or frame.offset_y + frame.height > stage[1]):
                raise ValueError("Frame exceeds the logical stage")
        animations.append(Animation(entry["name"], entry["fps"], frames))
    if len(animations) < 4:
        raise ValueError("At least four animations are required")
    return data, tuple(animations)
