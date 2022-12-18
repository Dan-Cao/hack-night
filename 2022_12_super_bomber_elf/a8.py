import asyncio
import json
import signal
import string

import curses
import websockets

sc = curses.initscr()
curses.noecho()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Wall
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # Opponent
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Self
curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Overlap
curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Dead
curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Bomb

COLOR_DEFAULT = curses.color_pair(1)
COLOR_WALL = curses.color_pair(2)
COLOR_OPPONENT = curses.color_pair(3)
COLOR_SELF = curses.color_pair(4)
COLOR_OVERLAP = curses.color_pair(5)
COLOR_DEAD = curses.color_pair(6)
COLOR_BOMB = curses.color_pair(7)

scr_h, scr_w = sc.getmaxyx()
win = curses.newwin(scr_h, scr_w, 0, 0)

win.keypad(1)
win.nodelay(True)
curses.curs_set(0)


def render_state(a):
    state = json.loads(a)

    board = []

    max_x = 0
    max_y = 0

    for w in state["walls"]:
        x = w["position"]["x"]
        y = w["position"]["y"]

        max_x = max(x, max_x)
        max_y = max(y, max_y)

    score_info_y_start = max_y + 2

    for i in range(0, max_y + 1):
        board.append([0] * (max_x + 1))
        win.addstr(i, 0, " " * max_x)

    for w in state["walls"]:
        x = w["position"]["x"]
        y = w["position"]["y"]

        if w["alive"]:
            board[y][x] += 1

        if w["type"] == "Strong":
            win.addch(y, x, curses.ACS_BLOCK)
        else:
            win.addch(y, x, curses.ACS_BLOCK, COLOR_WALL if w["alive"] else COLOR_DEAD)

    for i in range(score_info_y_start, scr_h - 1):
        win.addstr(i, 0, " " * scr_w)

    for i, p in enumerate(sorted(state["players"], key=lambda x_: x_["id"])):
        player_char = string.ascii_letters[i]
        if score_info_y_start + i < scr_h - 1:
            win.addstr(score_info_y_start + i, 0, f"{player_char} {p['name']} {p['score']}")

        x = p["position"]["x"]
        y = p["position"]["y"]

        if p["alive"]:
            board[y][x] += 1

        if p["name"] == "Dan":
            win.addch(
                y, x, curses.ACS_DIAMOND, COLOR_SELF if p["alive"] else COLOR_DEAD
            )
        else:
            win.addch(y, x, player_char, COLOR_OPPONENT if p["alive"] else COLOR_DEAD)

    for b in state["bombs"]:
        x = b["position"]["x"]
        y = b["position"]["y"]

        board[y][x] += 1
        if b["blast"]:
            blast = b["blast"]
            for b_x in range(x, x + blast["East"] + 1):
                win.addch(y, b_x, curses.ACS_CKBOARD, COLOR_BOMB)
            for b_x in range(x, x - blast["West"] - 1, -1):
                win.addch(y, b_x, curses.ACS_CKBOARD, COLOR_BOMB)
            for b_y in range(y, y + blast["South"] + 1):
                win.addch(b_y, x, curses.ACS_CKBOARD, COLOR_BOMB)
            for b_y in range(y, y - blast["North"] - 1, -1):
                win.addch(b_y, x, curses.ACS_CKBOARD, COLOR_BOMB)
        else:
            win.addch(y, x, curses.ACS_LANTERN, COLOR_BOMB)

    for p in state["players"]:
        x = p["position"]["x"]
        y = p["position"]["y"]

        if p["name"] == "Dan":
            color = COLOR_SELF
            if board[y][x] > 1:
                color = COLOR_OVERLAP
            if not p["alive"]:
                color = COLOR_DEAD

            win.addch(y, x, curses.ACS_DIAMOND, color)

    sc.refresh()


next_command = None
state = None
running = True


async def game():
    global next_command

    while running:
        if state:
            render_state(state)

        next_key = win.getch()
        if next_key == curses.ERR:
            pass
        elif next_key == ord("w"):
            next_command = '{"command":"MoveNorth"}'
        elif next_key == ord("a"):
            next_command = '{"command":"MoveWest"}'
        elif next_key == ord("s"):
            next_command = '{"command":"MoveSouth"}'
        elif next_key == ord("d"):
            next_command = '{"command":"MoveEast"}'
        elif next_key == ord(" "):
            next_command = '{"command":"DropBomb"}'

        await asyncio.sleep(0.01)


async def networking():
    async with websockets.connect("ws://localhost:8080") as ws:
        await ws.recv()
        await ws.send('{"command":["SetName","Dan"]}')

        global state
        global next_command

        while running:
            state = await ws.recv()

            command_to_send = next_command
            next_command = None

            if command_to_send:
                await ws.send(command_to_send)
            else:
                await ws.send('{"command": "Look"}')
                await asyncio.sleep(0.1)


async def main():
    task_1 = asyncio.create_task(game())
    task_2 = asyncio.create_task(networking())

    await asyncio.gather(task_1, task_2)


def handle_interrupt(signum, frame):
    global running
    running = False
    print("Exiting...")


signal.signal(signal.SIGINT, handle_interrupt)

asyncio.run(main())
