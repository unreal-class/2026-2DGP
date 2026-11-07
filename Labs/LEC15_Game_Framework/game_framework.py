running = False
stack = []


def change_mode(mode):
    if stack:
        stack.pop().finish()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    if stack:
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    if stack:
        stack.pop().finish()
    if stack:
        stack[-1].resume()
    else:
        quit()


def quit():
    global running
    running = False


def run(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    try:
        start_mode.init()
        while running:
            stack[-1].handle_events()
            stack[-1].update()
            stack[-1].render()
    finally:
        while stack:
            stack.pop().finish()
        running = False
