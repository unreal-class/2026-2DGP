"""Sprite rectangles use PNG coordinates (origin at the top left)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Frame:
    x: int
    y: int
    width: int
    height: int
    offset_x: int
    offset_y: int


@dataclass(frozen=True)
class Animation:
    name: str
    fps: float
    frames: tuple[Frame, ...]

    @property
    def duration(self):
        return len(self.frames) / self.fps
