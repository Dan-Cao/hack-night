import json

a = """{"bombs":[],"players":[{"alive":true,"id":"029c23d2-6702-4a8f-af73-d2d7e9bedffb","name":"Tony Chen","position":{"x":1,"y":4},"score":-1},{"alive":true,"id":"054219ff-163e-4652-8553-bfc83b70615b","name":"054219ff-163e-4652-8553-bfc83b70615b","position":{"x":9,"y":1},"score":0},{"alive":true,"id":"1091cafc-1199-498a-8cb8-0fd40e8d0acb","name":"1091cafc-1199-498a-8cb8-0fd40e8d0acb","position":{"x":1,"y":1},"score":0},{"alive":true,"id":"23fa1475-c4c8-452d-8e75-5b92f03256f0","name":"23fa1475-c4c8-452d-8e75-5b92f03256f0","position":{"x":1,"y":1},"score":0},{"alive":true,"id":"2a6d40cf-7aea-4688-847a-93de930c2c6c","name":"2a6d40cf-7aea-4688-847a-93de930c2c6c","position":{"x":1,"y":9},"score":0},{"alive":true,"id":"3ea9dbdd-468d-4cd7-9e0e-c904780f9e1f","name":"3ea9dbdd-468d-4cd7-9e0e-c904780f9e1f","position":{"x":1,"y":1},"score":0},{"alive":true,"id":"91eda073-4e0f-49af-b3f9-17bf0bd0221f","name":"java lads","position":{"x":9,"y":1},"score":0},{"alive":true,"id":"9a18e5a0-cff8-48b4-90d4-d8750a9e3935","name":"9a18e5a0-cff8-48b4-90d4-d8750a9e3935","position":{"x":9,"y":1},"score":0},{"alive":true,"id":"e1b0d519-551c-4580-a395-ebe06e2bb68b","name":"London Hack Night","position":{"x":6,"y":3},"score":-1}],"serverEndpoint":"ws://C02FC1D4MD6T:8080/","walls":[{"alive":true,"position":{"x":0,"y":0},"type":"Strong"},{"alive":true,"position":{"x":1,"y":0},"type":"Strong"},{"alive":true,"position":{"x":2,"y":0},"type":"Strong"},{"alive":true,"position":{"x":3,"y":0},"type":"Strong"},{"alive":true,"position":{"x":4,"y":0},"type":"Strong"},{"alive":true,"position":{"x":5,"y":0},"type":"Strong"},{"alive":true,"position":{"x":6,"y":0},"type":"Strong"},{"alive":true,"position":{"x":7,"y":0},"type":"Strong"},{"alive":true,"position":{"x":8,"y":0},"type":"Strong"},{"alive":true,"position":{"x":9,"y":0},"type":"Strong"},{"alive":true,"position":{"x":10,"y":0},"type":"Strong"},{"alive":true,"position":{"x":0,"y":10},"type":"Strong"},{"alive":true,"position":{"x":1,"y":10},"type":"Strong"},{"alive":true,"position":{"x":2,"y":10},"type":"Strong"},{"alive":true,"position":{"x":3,"y":10},"type":"Strong"},{"alive":true,"position":{"x":4,"y":10},"type":"Strong"},{"alive":true,"position":{"x":5,"y":10},"type":"Strong"},{"alive":true,"position":{"x":6,"y":10},"type":"Strong"},{"alive":true,"position":{"x":7,"y":10},"type":"Strong"},{"alive":true,"position":{"x":8,"y":10},"type":"Strong"},{"alive":true,"position":{"x":9,"y":10},"type":"Strong"},{"alive":true,"position":{"x":10,"y":10},"type":"Strong"},{"alive":true,"position":{"x":0,"y":0},"type":"Strong"},{"alive":true,"position":{"x":0,"y":1},"type":"Strong"},{"alive":true,"position":{"x":0,"y":2},"type":"Strong"},{"alive":true,"position":{"x":0,"y":3},"type":"Strong"},{"alive":true,"position":{"x":0,"y":4},"type":"Strong"},{"alive":true,"position":{"x":0,"y":5},"type":"Strong"},{"alive":true,"position":{"x":0,"y":6},"type":"Strong"},{"alive":true,"position":{"x":0,"y":7},"type":"Strong"},{"alive":true,"position":{"x":0,"y":8},"type":"Strong"},{"alive":true,"position":{"x":0,"y":9},"type":"Strong"},{"alive":true,"position":{"x":0,"y":10},"type":"Strong"},{"alive":true,"position":{"x":10,"y":0},"type":"Strong"},{"alive":true,"position":{"x":10,"y":1},"type":"Strong"},{"alive":true,"position":{"x":10,"y":2},"type":"Strong"},{"alive":true,"position":{"x":10,"y":3},"type":"Strong"},{"alive":true,"position":{"x":10,"y":4},"type":"Strong"},{"alive":true,"position":{"x":10,"y":5},"type":"Strong"},{"alive":true,"position":{"x":10,"y":6},"type":"Strong"},{"alive":true,"position":{"x":10,"y":7},"type":"Strong"},{"alive":true,"position":{"x":10,"y":8},"type":"Strong"},{"alive":true,"position":{"x":10,"y":9},"type":"Strong"},{"alive":true,"position":{"x":10,"y":10},"type":"Strong"},{"alive":true,"position":{"x":2,"y":2},"type":"Strong"},{"alive":true,"position":{"x":2,"y":4},"type":"Strong"},{"alive":true,"position":{"x":2,"y":6},"type":"Strong"},{"alive":true,"position":{"x":2,"y":8},"type":"Strong"},{"alive":true,"position":{"x":4,"y":2},"type":"Strong"},{"alive":true,"position":{"x":4,"y":4},"type":"Strong"},{"alive":true,"position":{"x":4,"y":6},"type":"Strong"},{"alive":true,"position":{"x":4,"y":8},"type":"Strong"},{"alive":true,"position":{"x":6,"y":2},"type":"Strong"},{"alive":true,"position":{"x":6,"y":4},"type":"Strong"},{"alive":true,"position":{"x":6,"y":6},"type":"Strong"},{"alive":true,"position":{"x":6,"y":8},"type":"Strong"},{"alive":true,"position":{"x":8,"y":2},"type":"Strong"},{"alive":true,"position":{"x":8,"y":4},"type":"Strong"},{"alive":true,"position":{"x":8,"y":6},"type":"Strong"},{"alive":true,"position":{"x":8,"y":8},"type":"Strong"},{"alive":true,"position":{"x":3,"y":1},"type":"Weak"},{"alive":true,"position":{"x":7,"y":1},"type":"Weak"},{"alive":true,"position":{"x":3,"y":5},"type":"Weak"},{"alive":true,"position":{"x":7,"y":5},"type":"Weak"},{"alive":true,"position":{"x":3,"y":9},"type":"Weak"},{"alive":true,"position":{"x":7,"y":9},"type":"Weak"},{"alive":true,"position":{"x":1,"y":3},"type":"Weak"},{"alive":true,"position":{"x":5,"y":3},"type":"Weak"},{"alive":true,"position":{"x":9,"y":3},"type":"Weak"},{"alive":false,"position":{"x":1,"y":7},"type":"Weak"},{"alive":true,"position":{"x":5,"y":7},"type":"Weak"},{"alive":true,"position":{"x":9,"y":7},"type":"Weak"}]}"""

state = json.loads(a)


def render_state(state):
    board = []
    for i in range(0, 11):
        board.append([" "] * 11)

    for w in state["walls"]:
        x = w["position"]["x"]
        y = w["position"]["y"]
        board[x][y] = "X" if w["type"] == "Strong" else "x"

    for p in state["players"]:
        x = p["position"]["x"]
        y = p["position"]["y"]
        board[x][y] = "o"

    for b in state["bombs"]:
        x = b["position"]["x"]
        y = b["position"]["y"]
        board[x][y] = "b"

    for row in board:
        for cell in row:
            print(cell, end="")
        print()


render_state(state)
