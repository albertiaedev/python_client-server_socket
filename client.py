import socket

FORMAT = "utf-8"

SERVER = "127.0.1.1"
PORT = 5050

ADDRESS = (SERVER,PORT)

HEADER = 64 #bits accepted in the first message the client sends
            #adjust in case your server needs a longer length

DISCONNECT = "!DISCONNECT"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDRESS)

def send(msg):
    message = msg.encode(FORMAT)
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength))
    client.send(sendLength)
    client.send(message)

send("Messaging...")
input()
send("Testing...")
input()
send("Testing...")
input()
send(DISCONNECT)
