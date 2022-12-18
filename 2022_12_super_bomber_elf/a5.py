import json
import string
import time

import curses

from websocket import create_connection

ws = None

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
        board.append([None] * (max_x + 1))
        win.addstr(i, 0, " " * max_x)

    for w in state["walls"]:
        x = w["position"]["x"]
        y = w["position"]["y"]

        if w["type"] == "Strong":
            win.addch(y, x, curses.ACS_BLOCK)
        else:
            win.addch(y, x, curses.ACS_BLOCK, COLOR_WALL if w["alive"] else COLOR_DEAD)

    for i in range(score_info_y_start, scr_h - 1):
        win.addstr(i, 0, " " * scr_w)

    for i, p in enumerate(sorted(state["players"], key=lambda x_: x_["id"])):
        player_char = string.ascii_letters[i]
        win.addstr(score_info_y_start + i, 0, f"{player_char} {p['name']} {p['score']}")

        x = p["position"]["x"]
        y = p["position"]["y"]

        if board[y][x] == "i":
            continue

        if p["name"] == "Dan":
            win.addch(
                y, x, curses.ACS_DIAMOND, COLOR_SELF if p["alive"] else COLOR_DEAD
            )
            board[y][x] = "i"
        else:
            win.addch(y, x, player_char, COLOR_OPPONENT if p["alive"] else COLOR_DEAD)

    for b in state["bombs"]:
        x = b["position"]["x"]
        y = b["position"]["y"]

        if b["blast"]:
            blast = b["blast"]
            for b_x in range(x, x + blast["East"] + 1):
                win.addch(y, b_x, "B", COLOR_BOMB)
            for b_x in range(x + 1, x - blast["West"] - 1, -1):
                win.addch(y, b_x, "B", COLOR_BOMB)
            for b_y in range(y, y + blast["South"] + 1):
                win.addch(b_y, x, "B", COLOR_BOMB)
            for b_y in range(y, y + blast["North"] - 1, -1):
                win.addch(b_y, x, "B", COLOR_BOMB)
        else:
            win.addch(y, x, curses.ACS_LANTERN, COLOR_BOMB)

    sc.refresh()


try:
    ws = create_connection("ws://localhost:8080/", timeout=5)
    print(ws.recv())
    ws.send('{"command":["SetName","Dan"]}')

    while True:
        state = ws.recv()
        render_state(state)

        next_command = '{"command": "Look"}'

        next_key = win.getch()

        if next_key == curses.ERR:
            time.sleep(0.1)
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

        ws.send(next_command)

finally:
    if ws:
        ws.close()
