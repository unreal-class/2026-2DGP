"""Build a tightly packed, variable-frame-size atlas from character.png.

Run this only to rebuild assets; the viewer does not need Pillow at runtime.
"""
import json
from pathlib import Path

from PIL import Image

from poses import ANIMATIONS, GROUND, STAGE_SIZE, pose

ROOT = Path(__file__).resolve().parent


def rotate_part(canvas, part, origin, pivot, angle):
    layer = Image.new("RGBA", canvas.size)
    layer.alpha_composite(part, tuple(map(round, origin)))
    layer = layer.rotate(angle, resample=Image.Resampling.NEAREST,
                         center=pivot)
    canvas.alpha_composite(layer)


def make_frame(source, motion):
    stage = Image.new("RGBA", STAGE_SIZE)
    x = STAGE_SIZE[0] // 2 - source.width // 2
    y = GROUND - source.height - round(motion["lift"])
    # Legs overlap the torso by two pixels so rotation cannot open a seam.
    legs = source.crop((14, 57, 37, 92))
    rotate_part(stage, legs, (x + 12, y + 57), (x + 24, y + 59), -motion["leg"])
    torso = source.crop((0, 0, 42, 60))
    # Reconstruct the shirt/waist behind the foreground arm using the
    # adjacent shirt pixels. Cutting away the shirt would leave a hole.
    torso.paste((0, 0, 0, 0), (18, 36, 28, 60))
    for row in range(36, 60):
        color = source.getpixel((28, row))
        torso.paste(color, (20, row, 28, row + 1))
    stage.alpha_composite(torso, (x, y))
    rotate_part(stage, legs, (x + 14, y + 57), (x + 25, y + 59), motion["leg"])
    arm = source.crop((18, 36, 27, 62))
    rotate_part(stage, arm, (x + 18, y + 36), (x + 23, y + 36), motion["arm"])
    if motion["lean"]:
        stage = stage.rotate(motion["lean"], Image.Resampling.NEAREST,
                             center=(64, GROUND - motion["lift"]))
    return stage


def build():
    source = Image.open(ROOT / "assets/character.png").convert("RGBA")
    atlas = Image.new("RGBA", (1024, 512))
    metadata = {"image": "character_sheet.png", "stage": STAGE_SIZE,
                "ground": GROUND, "animations": []}
    cursor_x = cursor_y = row_height = 0
    for name, count, fps in ANIMATIONS:
        animation = {"name": name, "fps": fps, "frames": []}
        for index in range(count):
            frame = make_frame(source, pose(name, index, count))
            bounds = frame.getbbox()
            if bounds is None:
                raise ValueError("Empty generated frame")
            cropped = frame.crop(bounds)
            if cursor_x + cropped.width + 2 > atlas.width:
                cursor_x = 0
                cursor_y += row_height + 2
                row_height = 0
            atlas.alpha_composite(cropped, (cursor_x, cursor_y))
            animation["frames"].append(dict(x=cursor_x, y=cursor_y,
                width=cropped.width, height=cropped.height,
                offset_x=bounds[0], offset_y=bounds[1]))
            cursor_x += cropped.width + 2
            row_height = max(row_height, cropped.height)
        metadata["animations"].append(animation)
    atlas.crop((0, 0, atlas.width, cursor_y + row_height)).save(
        ROOT / "assets/character_sheet.png")
    (ROOT / "assets/animations.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print("Built 31 frames across 4 animations.")


if __name__ == "__main__":
    build()
