"""Use a shared scale and origin to preserve motion between trimmed frames."""
WIDTH, HEIGHT = 960, 720


def stage_layout(animations, stage):
    frames = [frame for animation in animations for frame in animation.frames]
    # Even the smallest pose occupies at least half the canvas height.
    scale = (HEIGHT * 0.5) / min(frame.height for frame in frames)
    left = min(frame.offset_x for frame in frames)
    right = max(frame.offset_x + frame.width for frame in frames)
    top = min(frame.offset_y for frame in frames)
    bottom = max(frame.offset_y + frame.height for frame in frames)
    if (right - left) * scale > WIDTH - 80 or (bottom - top) * scale > HEIGHT - 130:
        raise ValueError("Animation bounds do not fit the canvas")
    origin_x = WIDTH / 2 - (left + right) * scale / 2
    origin_y = HEIGHT / 2 + (top + bottom) * scale / 2 - 5
    return scale, origin_x, origin_y


def draw_rect(frame, layout):
    scale, origin_x, origin_y = layout
    return (round(origin_x + (frame.offset_x + frame.width / 2) * scale),
            round(origin_y - (frame.offset_y + frame.height / 2) * scale),
            round(frame.width * scale), round(frame.height * scale))
