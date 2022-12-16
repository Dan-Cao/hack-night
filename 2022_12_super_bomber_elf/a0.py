from websocket import create_connection

ws = None
try:
    ws = create_connection("ws://localhost:8080/")
    while True:
        print(ws.recv())

        command = input("enter command: ")
        ws.send(command)
finally:
    if ws:
        ws.close()
