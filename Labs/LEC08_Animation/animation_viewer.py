from pathlib import Path
from time import monotonic

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_SIZE = 128
SHEET_HEIGHT = 2048
FRAME_DURATION = 0.1
REPEAT_COUNT = 5
PAUSE_DURATION = 1.0
ASSET_PATH = Path(__file__).with_name('spelunky_animation_sheet.png')
ROW_COLUMNS = {
	0: range(16),
	1: tuple(range(12)) + (13, 14),
	2: range(15),
	3: range(15),
	4: tuple(range(11)) + tuple(range(12, 16)),
	5: range(15),
	6: tuple(range(12)) + (13, 14),
	7: range(15),
	8: range(15),
	9: range(16),
	10: range(16),
	11: range(11),
}


def frame_rect(row, column, width=FRAME_SIZE, height=FRAME_SIZE):
	bottom = SHEET_HEIGHT - (row + 1) * FRAME_SIZE
	return column * FRAME_SIZE, bottom, width, height



def row_frames(row, columns=None):
	if columns is None:
		columns = ROW_COLUMNS[row]
	return [frame_rect(row, column) for column in columns]


LEDGE_WOBBLE_FRAMES = row_frames(3, range(11))
LEDGE_HANG_FRAMES = row_frames(3, range(11, 15))
ROPE_FRAMES = row_frames(7, range(10))
CROUCH_STAND_FRAMES = row_frames(7, range(10, 15))


ANIMATIONS = [
	{'name': '걷기 / 수영', 'frames': row_frames(0)},
	{'name': '숙이기 / 숙여서 이동', 'frames': row_frames(1)},
	{'name': '피해 / 쓰러지기', 'frames': row_frames(2, range(4))},
	{'name': '절벽 비틀거림 / 매달리기', 'frames': LEDGE_WOBBLE_FRAMES + LEDGE_HANG_FRAMES},
	{'name': '던지기', 'frames': row_frames(4)},
	{'name': '문 들어가기 / 나오기', 'frames': row_frames(5)},
	{'name': '사다리 / 밀기', 'frames': row_frames(6)},
	{'name': '밧줄 / 숙였다 일어서기', 'frames': ROPE_FRAMES + CROUCH_STAND_FRAMES},
	{'name': '위 보기', 'frames': row_frames(8)},
	{'name': '점프', 'frames': row_frames(9)},
	{'name': '유령 이동 / 발사', 'frames': row_frames(10)},
	{'name': '낙하', 'frames': row_frames(11)},
]

KEY_TO_ANIMATION = {
	SDLK_1: 0,
	SDLK_2: 1,
	SDLK_3: 2,
	SDLK_4: 3,
	SDLK_5: 4,
	SDLK_6: 5,
	SDLK_7: 6,
	SDLK_8: 7,
	SDLK_9: 8,
	SDLK_0: 9,
	SDLK_KP_1: 10,
	SDLK_KP_2: 11,
}


def reset_playback_state(animation_index, now):
	return {
		'animation_index': animation_index,
		'frame_index': 0,
		'repeat_count': 0,
		'last_frame_time': now,
		'pause_until': 0.0,
	}


def handle_keydown(key, state, now):
	if key == SDLK_ESCAPE:
		return False, state

	animation_index = KEY_TO_ANIMATION.get(key)
	if key == SDLK_UP:
		animation_index = 8
	if animation_index is not None:
		state = reset_playback_state(animation_index, now)
	return True, state


def advance_playback(state, now):
	if state['pause_until']:
		if now < state['pause_until']:
			return state
		next_animation = (state['animation_index'] + 1) % len(ANIMATIONS)
		state = reset_playback_state(next_animation, now)

	if now - state['last_frame_time'] < FRAME_DURATION:
		return state

	state['last_frame_time'] = now
	state['frame_index'] += 1
	if state['frame_index'] >= len(ANIMATIONS[state['animation_index']]['frames']):
		state['frame_index'] = 0
		state['repeat_count'] += 1
		if state['repeat_count'] >= REPEAT_COUNT:
			state['repeat_count'] = 0
			state['pause_until'] = now + PAUSE_DURATION
	return state


def draw_frame(sprite_sheet, state):
	clear_canvas()
	left, bottom, width, height = ANIMATIONS[state['animation_index']]['frames'][state['frame_index']]
	display_size = max(FRAME_SIZE * 2, CANVAS_HEIGHT * 0.6)
	sprite_sheet.clip_draw(
		left,
		bottom,
		width,
		height,
		CANVAS_WIDTH // 2,
		CANVAS_HEIGHT // 2,
		display_size,
		display_size,
	)
	update_canvas()


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	sprite_sheet = load_image(str(ASSET_PATH))
	state = reset_playback_state(0, monotonic())
	running = True

	try:
		while running:
			now = monotonic()
			for event in get_events():
				if event.type == SDL_QUIT:
					running = False
				elif event.type == SDL_KEYDOWN:
					running, state = handle_keydown(event.key, state, now)

			if running:
				state = advance_playback(state, now)
				draw_frame(sprite_sheet, state)
				delay(1 / 60)
	finally:
		close_canvas()


if __name__ == '__main__':
	main()
