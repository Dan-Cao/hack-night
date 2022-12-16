import json
import time

import win32api

from websocket import create_connection

ws = None


def render_state(a):
    print("\n" * 100)
    state = json.loads(a)

    board = []

    max_x = 0
    max_y = 0

    for w in state["walls"]:
        x = w["position"]["x"]
        y = w["position"]["y"]

        max_x = max(x, max_x)
        max_y = max(y, max_y)

    for i in range(0, max_y + 1):
        board.append([" "] * (max_x + 1))

    for w in state["walls"]:
        x = w["position"]["x"]
        y = w["position"]["y"]

        if not w["alive"]:
            continue

        board[y][x] = "X" if w["type"] == "Strong" else "x"

    for p in state["players"]:
        x = p["position"]["x"]
        y = p["position"]["y"]

        if board[y][x] == "i":
            continue
        if not p["alive"]:
            continue

        board[y][x] = "i" if p["name"] == "Dan" else "o"

    for b in state["bombs"]:
        x = b["position"]["x"]
        y = b["position"]["y"]
        board[y][x] = "b"

    for row in board:
        for cell in row:
            print(cell, end="")
        print()


try:
    ws = create_connection("ws://localhost:8080/", timeout=5)
    print(ws.recv())
    ws.send('{"command":["SetName","Dan"]}')

    while True:
        state = ws.recv()
        render_state(state)

        next_command = '{"command": "Look"}'

        if win32api.GetAsyncKeyState(ord('W')):
            next_command = '{"command":"MoveNorth"}'
        if win32api.GetAsyncKeyState(ord('A')):
            next_command = '{"command":"MoveWest"}'
        if win32api.GetAsyncKeyState(ord('S')):
            next_command = '{"command":"MoveSouth"}'
        if win32api.GetAsyncKeyState(ord('D')):
            next_command = '{"command":"MoveEast"}'
        if win32api.GetAsyncKeyState(ord(' ')):
            next_command = '{"command":"DropBomb"}'

        ws.send(next_command)
        time.sleep(0.5)

finally:
    if ws:
        ws.close()
