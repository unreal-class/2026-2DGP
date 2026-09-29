"""Exercise the real SDL renderer; optionally save a contact sheet for review."""
import argparse
import ctypes

from PIL import Image
import pico2d as p

from layout import HEIGHT, WIDTH, stage_layout
from loading import ASSETS, load_animations
from playback import PlaybackState
from rendering import load_ui_font, render


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="Optional PNG contact sheet path")
    args = parser.parse_args()
    data, animations = load_animations()
    layout = stage_layout(animations, data["stage"])
    contact = Image.new("RGB", (WIDTH * 2, HEIGHT * 2))
    p.open_canvas(WIDTH, HEIGHT)
    try:
        sheet = p.load_image(str(ASSETS / data["image"]))
        font = load_ui_font()
        for index, animation in enumerate(animations):
            sample = len(animation.frames) // (4 if index < 2 else 2)
            state = PlaybackState(index, sample, 3, False, 0.5)
            render(sheet, font, animations, state, layout, present=False)
            pixels = (ctypes.c_ubyte * (WIDTH * HEIGHT * 4))()
            # pico2d keeps its SDL renderer in its implementation module.
            renderer = p.clear_canvas.__globals__["renderer"]
            result = p.SDL_RenderReadPixels(renderer, None, p.SDL_PIXELFORMAT_RGBA32,
                                          pixels, WIDTH * 4)
            if result != 0:
                raise RuntimeError("SDL could not read the rendered frame")
            frame = Image.frombytes("RGBA", (WIDTH, HEIGHT), bytes(pixels))
            contact.paste(frame.convert("RGB"), ((index % 2) * WIDTH, (index // 2) * HEIGHT))
            p.update_canvas()
            p.get_events()
        if args.output:
            contact.save(args.output)
        print("Rendered all four actions successfully.")
    finally:
        p.close_canvas()


if __name__ == "__main__":
    main()
