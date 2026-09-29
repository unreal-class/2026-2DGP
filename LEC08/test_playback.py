import unittest

from loading import load_animations
from playback import PAUSE_SECONDS, REPEATS, state_at


class PlaybackTests(unittest.TestCase):
    def setUp(self):
        _, self.animations = load_animations()

    def test_every_frame_of_all_five_repetitions(self):
        offset = 0
        for index, animation in enumerate(self.animations):
            count = len(animation.frames)
            for tick in range(count * REPEATS):
                state = state_at(self.animations, offset + (tick + 0.5) / animation.fps)
                self.assertEqual((state.animation, state.frame, state.repetition, state.holding),
                                 (index, tick % count, tick // count + 1, False))
            offset += animation.duration * REPEATS + PAUSE_SECONDS

    def test_holds_last_frame_for_one_second(self):
        offset = 0
        for index, animation in enumerate(self.animations):
            end = offset + animation.duration * REPEATS
            self.assertFalse(state_at(self.animations, end - 1e-6).holding)
            for delta in (1e-6, 0.5, 1 - 1e-6):
                state = state_at(self.animations, end + delta)
                self.assertEqual((state.animation, state.frame, state.holding),
                                 (index, len(animation.frames) - 1, True))
            offset = end + PAUSE_SECONDS
            state = state_at(self.animations, offset + 1e-6)
            self.assertEqual((state.animation, state.frame, state.holding),
                             ((index + 1) % len(self.animations), 0, False))

    def test_large_time_jump_wraps_without_drift(self):
        total = sum(a.duration * REPEATS + PAUSE_SECONDS for a in self.animations)
        expected = state_at(self.animations, 0.25)
        for cycles in (1, 100, 100000):
            actual = state_at(self.animations, cycles * total + 0.25)
            self.assertEqual((actual.animation, actual.frame, actual.repetition),
                             (expected.animation, expected.frame, expected.repetition))

    def test_invalid_time_rejected(self):
        for elapsed in (-1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                state_at(self.animations, elapsed)


if __name__ == "__main__":
    unittest.main()
