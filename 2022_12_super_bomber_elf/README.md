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

[a4.py](a4.py) - eliminates screen flashing by rendering using curses

* Also adds colours and symbols for improved readability

[a5.py](a5.py) - list player scores and add differentiating symbols for each player

[a6.py](a6.py) - prevent input queuing by separating game and network loops

* Achieved by making the client async

[a7.py](a7.py) - indicate when there is something else active under the player
