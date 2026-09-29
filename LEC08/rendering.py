"""Pico2d rendering, kept separate from the deterministic playback clock."""
from pathlib import Path
import os

import pico2d as p

from layout import WIDTH, HEIGHT, draw_rect


def load_ui_font():
    candidates = [Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts/arial.ttf",
                  Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
                  Path("/System/Library/Fonts/Supplemental/Arial.ttf")]
    for candidate in candidates:
        if candidate.exists():
            return p.load_font(str(candidate), 22)
    return None


def render(sheet, font, animations, state, layout, present=True):
    p.clear_canvas()
    p.draw_rectangle(0, 0, WIDTH, HEIGHT, 22, 29, 41, filled=True)
    p.draw_rectangle(30, 76, WIDTH - 30, HEIGHT - 100, 29, 39, 53, filled=True)
    animation = animations[state.animation]
    frame = animation.frames[state.frame]
    sheet.clip_draw(frame.x, sheet.h - frame.y - frame.height,
                    frame.width, frame.height, *draw_rect(frame, layout))
    if font:
        font.draw(32, HEIGHT - 36, "CHARACTER / ANIMATION VIEWER", (234, 240, 249))
        status = "HOLD 1s" if state.holding else f"LOOP {state.repetition}/5"
        font.draw(32, HEIGHT - 72,
                  f"{state.animation + 1}/4  {animation.name.upper()}    {status}",
                  (100, 221, 187))
        font.draw(32, 47, "Walk  >  Run  >  Jump  >  Attack", (180, 193, 210))
        font.draw(WIDTH - 170, 47, "ESC: close", (180, 193, 210))
    p.draw_rectangle(32, 20, WIDTH - 32, 25, 52, 65, 80, filled=True)
    if state.progress > 0:
        p.draw_rectangle(32, 20, 32 + int((WIDTH - 64) * state.progress), 25,
                         100, 221, 187, filled=True)
    if present:
        p.update_canvas()
