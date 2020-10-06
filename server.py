import socket
from _thread import *


server = "192.168.0.101"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# currently implemented as: max 3 players
s.listen(3)
print("Waiting for Connections, Server Started:", (server, port))

currentplayer = 0
clientlist = []

def threaded_client(conn, player):
    print()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentplayer))
    currentplayer += 1