# Chaussette 

Video capture app on top of a websocket client that dialogs with [a node.js server](https://github.com/esadpyrenees/chaussettejs).

### Requirements

Python > 3.8

### Installation

```bash
# create a virtualenv
python -m venv env
# activate virtualenv
source env/bin/activate
# install dependencies
pip install -r requirements.txt
```

### Setup and run

The node.js server should be up and running.

Configure its IP address (`server_ip`) in `chaussette.py`:

```py
server_ip = "192.168.2.101"
```
Launch programm.
```bash
# set executable
chmod +x main.py
# run
./main.py
```
