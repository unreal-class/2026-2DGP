import unittest

from PIL import Image

from generate_sheet import make_frame
from loading import ASSETS, load_animations
from poses import pose


class AssetTests(unittest.TestCase):
    def test_atlas_reconstructs_authored_frames_exactly(self):
        data, animations = load_animations()
        with Image.open(ASSETS / data["image"]) as atlas, Image.open(ASSETS / "character.png") as source:
            sizes = set()
            counts = set()
            for animation in animations:
                counts.add(len(animation.frames))
                for index, frame in enumerate(animation.frames):
                    self.assertLessEqual(frame.x + frame.width, atlas.width)
                    self.assertLessEqual(frame.y + frame.height, atlas.height)
                    sizes.add((frame.width, frame.height))
                    cropped = atlas.crop((frame.x, frame.y, frame.x + frame.width, frame.y + frame.height))
                    rebuilt = Image.new("RGBA", tuple(data["stage"]))
                    rebuilt.alpha_composite(cropped, (frame.offset_x, frame.offset_y))
                    expected = make_frame(source.convert("RGBA"), pose(animation.name, index, len(animation.frames)))
                    self.assertEqual(rebuilt.tobytes(), expected.tobytes())
            self.assertGreater(len(sizes), 1)
            self.assertEqual(counts, {6, 7, 8, 10})

    def test_actions_have_distinct_poses_and_no_stage_clipping(self):
        _, animations = load_animations()
        with Image.open(ASSETS / "character.png") as source:
            for animation in animations:
                poses = []
                for index in range(len(animation.frames)):
                    frame = make_frame(source.convert("RGBA"), pose(animation.name, index, len(animation.frames)))
                    x1, y1, x2, y2 = frame.getbbox()
                    self.assertGreater(min(x1, y1), 0)
                    self.assertLess(x2, frame.width)
                    self.assertLess(y2, frame.height)
                    poses.append(frame.tobytes())
                self.assertGreater(len(set(poses)), 2)


if __name__ == "__main__":
    unittest.main()
