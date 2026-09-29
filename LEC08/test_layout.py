import unittest

from layout import HEIGHT, WIDTH, draw_rect, stage_layout
from loading import load_animations


class LayoutTests(unittest.TestCase):
    def test_all_poses_are_large_and_inside_the_stage_panel(self):
        data, animations = load_animations()
        layout = stage_layout(animations, data["stage"])
        for animation in animations:
            for frame in animation.frames:
                x, y, width, height = draw_rect(frame, layout)
                self.assertGreaterEqual(height, HEIGHT / 2)
                self.assertGreaterEqual(x - width / 2, 30)
                self.assertLessEqual(x + width / 2, WIDTH - 30)
                self.assertGreaterEqual(y - height / 2, 76)
                self.assertLessEqual(y + height / 2, HEIGHT - 100)

    def test_trim_offsets_preserve_common_origin(self):
        data, animations = load_animations()
        layout = stage_layout(animations, data["stage"])
        scale, origin_x, origin_y = layout
        for animation in animations:
            for frame in animation.frames:
                x, y, width, height = draw_rect(frame, layout)
                self.assertAlmostEqual(x - (frame.offset_x + frame.width / 2) * scale, origin_x, delta=0.51)
                self.assertAlmostEqual(y + (frame.offset_y + frame.height / 2) * scale, origin_y, delta=0.51)


if __name__ == "__main__":
    unittest.main()
