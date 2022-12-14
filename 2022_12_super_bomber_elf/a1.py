import readchar
from websocket import create_connection

ws = None
try:
    ws = create_connection("ws://172.16.173.86:8080/")
    while True:
        print(ws.recv())

        ws.send('{"command":["SetName","Dan"]}')
        print(ws.recv())

        command = readchar.readkey()
        match command:
            case "w":
                ws.send('{"command":"MoveNorth"}')
            case "a":
                ws.send('{"command":"MoveWest"}')
            case "s":
                ws.send('{"command":"MoveSouth"}')
            case "d":
                ws.send('{"command":"MoveEast"}')
            case " ":
                ws.send('{"command":"DropBomb"}')

finally:
    if ws:
        ws.close()
