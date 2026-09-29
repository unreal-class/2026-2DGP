"""Elapsed-time playback: five cycles, one-second hold, next action forever."""
from dataclasses import dataclass
from math import isfinite

REPEATS = 5
PAUSE_SECONDS = 1.0


@dataclass(frozen=True)
class PlaybackState:
    animation: int
    frame: int
    repetition: int
    holding: bool
    progress: float


def state_at(animations, elapsed):
    if not animations or not isfinite(elapsed) or elapsed < 0:
        raise ValueError("Expected animations and finite nonnegative elapsed time")
    durations = [animation.duration * REPEATS for animation in animations]
    total = sum(duration + PAUSE_SECONDS for duration in durations)
    position = elapsed % total
    for index, (animation, duration) in enumerate(zip(animations, durations)):
        if position < duration + PAUSE_SECONDS:
            if position >= duration:
                return PlaybackState(index, len(animation.frames) - 1,
                                     REPEATS, True, 1.0)
            tick = min(int(position * animation.fps),
                       len(animation.frames) * REPEATS - 1)
            return PlaybackState(index, tick % len(animation.frames),
                                 tick // len(animation.frames) + 1, False,
                                 position / duration)
        position -= duration + PAUSE_SECONDS
    # Protect against a rounding residual at the wrap boundary.
    return PlaybackState(0, 0, 1, False, 0.0)
