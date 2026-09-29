"""Hand-authored motion curves for the supplied single-pose character.

Angles rotate the cutout parts; jump height is measured in source pixels.
This is cutout animation, not a claim that the original PNG had extra poses.
"""
from math import cos, pi, sin

ANIMATIONS = (("Walk", 8, 10), ("Run", 6, 14),
              ("Jump", 10, 12), ("Attack", 7, 12))
STAGE_SIZE = (128, 144)
GROUND = 132


def pose(name, index, count):
    phase = 2 * pi * index / count
    stride = sin(phase)
    if name == "Walk":
        return dict(leg=24 * stride, arm=-20 * stride,
                    lift=2 * (1 - cos(phase * 2)), lean=0)
    if name == "Run":
        return dict(leg=48 * stride, arm=-48 * stride,
                    lift=5 * (1 - cos(phase * 2)), lean=-8)
    if name == "Jump":
        progress = index / (count - 1)
        height = sin(pi * progress)
        return dict(leg=30 * height, arm=-125 * height,
                    lift=30 * height, lean=0)
    if name == "Attack":
        angles = (0, -35, -65, 80, 100, 55, 0)
        return dict(leg=10 * sin(pi * index / (count - 1)),
                    arm=angles[index], lift=0,
                    lean=-8 if index in (3, 4) else 0)
    raise ValueError(f"Unknown animation: {name}")
