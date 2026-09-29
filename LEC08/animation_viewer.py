"""Drill 8: python LEC08/animation_viewer.py (Escape to exit)."""
import argparse
from time import perf_counter

from layout import HEIGHT, WIDTH, stage_layout
from loading import ASSETS, load_animations
from playback import state_at


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate metadata without a window")
    parser.add_argument("--seconds", type=float, default=None,
                        help="Exit after this many seconds (for smoke testing)")
    args = parser.parse_args()
    if args.seconds is not None and args.seconds <= 0:
        parser.error("--seconds must be positive")
    data, animations = load_animations()
    layout = stage_layout(animations, data["stage"])
    if args.check:
        print("Validated:", ", ".join(f"{a.name} ({len(a.frames)} frames)" for a in animations))
        return
    import pico2d as p
    from rendering import load_ui_font, render
    p.open_canvas(WIDTH, HEIGHT, sync=True)
    try:
        sheet = p.load_image(str(ASSETS / data["image"]))
        for animation in animations:
            for frame in animation.frames:
                if frame.x + frame.width > sheet.w or frame.y + frame.height > sheet.h:
                    raise ValueError("A frame extends beyond the sprite sheet")
        font = load_ui_font()
        start = perf_counter()
        while True:
            events = p.get_events()
            if any(event.type == p.SDL_QUIT or
                   (event.type == p.SDL_KEYDOWN and event.key == p.SDLK_ESCAPE)
                   for event in events):
                break
            elapsed = perf_counter() - start
            if args.seconds is not None and elapsed >= args.seconds:
                break
            render(sheet, font, animations, state_at(animations, elapsed), layout)
            p.delay(0.001)
    finally:
        p.close_canvas()


if __name__ == "__main__":
    main()
