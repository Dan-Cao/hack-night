from websocket import create_connection

ws = None
try:
    ws = create_connection("ws://172.16.173.86:8080/")
    while True:
        print(ws.recv())

        command = input("enter command: ")
        ws.send(command)
finally:
    if ws:
        ws.close()
