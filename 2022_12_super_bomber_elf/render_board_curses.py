import json
import time

import curses

a = """{"bombs":[{"blast":{"East":1,"North":1,"South":2,"West":2},"position":{"x":9,"y":1}}],"players":[{"alive":false,"id":"7153136b-5af0-418a-866d-09beece7e6a2","name":"WLHN","position":{"x":9,"y":2},"score":-1},{"alive":true,"id":"bcaac00b-83c1-4c89-abba-b4d2775696be","name":"Dan","position":{"x":2,"y":1},"score":-3}],"walls":[{"alive":true,"position":{"x":0,"y":0},"type":"Strong"},{"alive":true,"position":{"x":1,"y":0},"type":"Strong"},{"alive":true,"position":{"x":2,"y":0},"type":"Strong"},{"alive":true,"position":{"x":3,"y":0},"type":"Strong"},{"alive":true,"position":{"x":4,"y":0},"type":"Strong"},{"alive":true,"position":{"x":5,"y":0},"type":"Strong"},{"alive":true,"position":{"x":6,"y":0},"type":"Strong"},{"alive":true,"position":{"x":7,"y":0},"type":"Strong"},{"alive":true,"position":{"x":8,"y":0},"type":"Strong"},{"alive":true,"position":{"x":9,"y":0},"type":"Strong"},{"alive":true,"position":{"x":10,"y":0},"type":"Strong"},{"alive":true,"position":{"x":0,"y":10},"type":"Strong"},{"alive":true,"position":{"x":1,"y":10},"type":"Strong"},{"alive":true,"position":{"x":2,"y":10},"type":"Strong"},{"alive":true,"position":{"x":3,"y":10},"type":"Strong"},{"alive":true,"position":{"x":4,"y":10},"type":"Strong"},{"alive":true,"position":{"x":5,"y":10},"type":"Strong"},{"alive":true,"position":{"x":6,"y":10},"type":"Strong"},{"alive":true,"position":{"x":7,"y":10},"type":"Strong"},{"alive":true,"position":{"x":8,"y":10},"type":"Strong"},{"alive":true,"position":{"x":9,"y":10},"type":"Strong"},{"alive":true,"position":{"x":10,"y":10},"type":"Strong"},{"alive":true,"position":{"x":0,"y":0},"type":"Strong"},{"alive":true,"position":{"x":0,"y":1},"type":"Strong"},{"alive":true,"position":{"x":0,"y":2},"type":"Strong"},{"alive":true,"position":{"x":0,"y":3},"type":"Strong"},{"alive":true,"position":{"x":0,"y":4},"type":"Strong"},{"alive":true,"position":{"x":0,"y":5},"type":"Strong"},{"alive":true,"position":{"x":0,"y":6},"type":"Strong"},{"alive":true,"position":{"x":0,"y":7},"type":"Strong"},{"alive":true,"position":{"x":0,"y":8},"type":"Strong"},{"alive":true,"position":{"x":0,"y":9},"type":"Strong"},{"alive":true,"position":{"x":0,"y":10},"type":"Strong"},{"alive":true,"position":{"x":10,"y":0},"type":"Strong"},{"alive":true,"position":{"x":10,"y":1},"type":"Strong"},{"alive":true,"position":{"x":10,"y":2},"type":"Strong"},{"alive":true,"position":{"x":10,"y":3},"type":"Strong"},{"alive":true,"position":{"x":10,"y":4},"type":"Strong"},{"alive":true,"position":{"x":10,"y":5},"type":"Strong"},{"alive":true,"position":{"x":10,"y":6},"type":"Strong"},{"alive":true,"position":{"x":10,"y":7},"type":"Strong"},{"alive":true,"position":{"x":10,"y":8},"type":"Strong"},{"alive":true,"position":{"x":10,"y":9},"type":"Strong"},{"alive":true,"position":{"x":10,"y":10},"type":"Strong"},{"alive":true,"position":{"x":2,"y":2},"type":"Strong"},{"alive":true,"position":{"x":2,"y":4},"type":"Strong"},{"alive":true,"position":{"x":2,"y":6},"type":"Strong"},{"alive":true,"position":{"x":2,"y":8},"type":"Strong"},{"alive":true,"position":{"x":4,"y":2},"type":"Strong"},{"alive":true,"position":{"x":4,"y":4},"type":"Strong"},{"alive":true,"position":{"x":4,"y":6},"type":"Strong"},{"alive":true,"position":{"x":4,"y":8},"type":"Strong"},{"alive":true,"position":{"x":6,"y":2},"type":"Strong"},{"alive":true,"position":{"x":6,"y":4},"type":"Strong"},{"alive":true,"position":{"x":6,"y":6},"type":"Strong"},{"alive":true,"position":{"x":6,"y":8},"type":"Strong"},{"alive":true,"position":{"x":8,"y":2},"type":"Strong"},{"alive":true,"position":{"x":8,"y":4},"type":"Strong"},{"alive":true,"position":{"x":8,"y":6},"type":"Strong"},{"alive":true,"position":{"x":8,"y":8},"type":"Strong"},{"alive":false,"position":{"x":3,"y":1},"type":"Weak"},{"alive":false,"position":{"x":7,"y":1},"type":"Weak"},{"alive":true,"position":{"x":3,"y":5},"type":"Weak"},{"alive":true,"position":{"x":7,"y":5},"type":"Weak"},{"alive":true,"position":{"x":3,"y":9},"type":"Weak"},{"alive":true,"position":{"x":7,"y":9},"type":"Weak"},{"alive":false,"position":{"x":1,"y":3},"type":"Weak"},{"alive":true,"position":{"x":5,"y":3},"type":"Weak"},{"alive":false,"position":{"x":9,"y":3},"type":"Weak"},{"alive":true,"position":{"x":1,"y":7},"type":"Weak"},{"alive":true,"position":{"x":5,"y":7},"type":"Weak"},{"alive":true,"position":{"x":9,"y":7},"type":"Weak"}]}"""

state = json.loads(a)

# initialize screen
sc = curses.initscr()

curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Wall
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # Opponent
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Self
curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)  # ???
curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Dead
curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Bomb

COLOR_WALL = curses.color_pair(2)
COLOR_OPPONENT = curses.color_pair(3)
COLOR_SELF = curses.color_pair(4)
COLOR_DEAD = curses.color_pair(6)
COLOR_BOMB = curses.color_pair(7)

h, w = sc.getmaxyx()
win = curses.newwin(h, w, 0, 0)

win.keypad(1)
curses.curs_set(0)


def render_state(state):
    board = []
    for i in range(0, 11):
        board.append([" "] * 11)

    for w in state["walls"]:
        x = w["position"]["x"]
        y = w["position"]["y"]

        if w["type"] == "Strong":
            win.addch(y, x, curses.ACS_BLOCK)
        else:
            win.addch(y, x, curses.ACS_BLOCK, COLOR_WALL)

    for p in state["players"]:
        x = p["position"]["x"]
        y = p["position"]["y"]

        if board[y][x] == "i":
            continue

        if p["name"] == "Dan":
            win.addch(y, x, curses.ACS_DIAMOND, COLOR_SELF if p["alive"] else COLOR_DEAD)
            board[y][x] = "i"
        else:
            win.addch(y, x, "O", COLOR_OPPONENT if p["alive"] else COLOR_DEAD)

    for b in state["bombs"]:
        x = b["position"]["x"]
        y = b["position"]["y"]

        if b["blast"]:
            win.addch(y, x, "B", COLOR_BOMB)

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

    win.refresh()


render_state(state)

time.sleep(10)
