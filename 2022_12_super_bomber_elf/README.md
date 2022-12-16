# Super Bomber Elf

Python client for https://github.com/krisajenkins/SuperBomberElf

## What are the different files?

[a0.py](a0.py) - a basic Websocket client

* Requires full command to be typed and Enter to pressed after every command

[a1.py](a1.py) - allows control by pressing WASD or space

* Also sets the username

[a2.py](a2.py) - attempts to render the game board

* Requires keypress in order for game to update due to blocking keyboard I/O
* Also builds up a queue of inputs if the server is slow leading to "lag"

[a3.py](a3.py) - allows the board to update independently without any input

* Only works with Windows due to use of the `win32api.GetAsyncKeyState` API
