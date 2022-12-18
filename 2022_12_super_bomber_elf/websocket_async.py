import asyncio
import websockets

ws = None


async def hello():
    async with websockets.connect("ws://localhost:8080") as ws:
        msg = await ws.recv()
        print(msg)


asyncio.run(hello())
