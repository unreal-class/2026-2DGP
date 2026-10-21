import math

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_TIME = 0.01


class CharacterAnimation:
	def __init__(self, character):
		self.character = character
		self.x = CANVAS_WIDTH // 2
		self.y = CANVAS_HEIGHT // 2
		self.phase = "circle"
		self.step = 0

	def update(self):
		if self.phase == "circle":
			self.step += 1
			angle = math.radians(self.step)
			self.x = 400 + 150 * math.cos(angle)
			self.y = 300 + 150 * math.sin(angle)
			if self.step > 360:
				self.phase = "rectangle"
				self.step = 0
			return

		if self.phase == "rectangle":
			self.step += 1
			distance = 300
			half_height = distance // 2
			if self.step <= half_height:
				self.x = 550
				self.y = 300 + self.step
			elif self.step <= half_height + distance:
				self.x = 550 - (self.step - half_height)
				self.y = 450
			elif self.step <= half_height + distance * 2:
				self.x = 250
				self.y = 450 - (self.step - half_height - distance)
			elif self.step <= half_height + distance * 3:
				self.x = 250 + (self.step - half_height - distance * 2)
				self.y = 150
			else:
				self.x = 550
				self.y = 150 + (self.step - half_height - distance * 3)
				self.phase = "triangle"
				self.step = 0
			return

		self.step += 1
		triangle_width = 300
		triangle_height = 150
		if self.step <= triangle_width // 2:
			self.x = 550 - self.step
			self.y = 300 + triangle_height * self.step / (triangle_width // 2)
		elif self.step <= triangle_width:
			progress = self.step - triangle_width // 2
			self.x = 400 - progress
			self.y = 450 - triangle_height * progress / (triangle_width // 2)
		else:
			self.x = 250 + (self.step - triangle_width)
			self.y = 300
			if self.step >= triangle_width * 2:
				self.phase = "circle"
				self.step = 0

	def draw(self):
		self.character.draw(self.x, self.y)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
character = load_image("character.png")
animation = CharacterAnimation(character)
running = True

while running:
	for event in get_events():
		if event.type == SDL_QUIT:
			running = False

	animation.update()
	clear_canvas()
	animation.draw()
	update_canvas()
	delay(FRAME_TIME)

close_canvas()