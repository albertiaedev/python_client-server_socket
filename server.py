import socket
import threading

FORMAT = "utf-8"

server_name = input("SERVER NAME: ")
PORT = 5050

#SERVER = ###insert your server's ipv4###
          ###(public IP address) between quotes here###
    #or#
SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER,PORT)

HEADER = 64 #bits accepted in the first message the client sends
            #adjust in case your server needs a longer length

DISCONNECT = "!DISCONNECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)

def client(conn,addr):
    print(f"NEW CONNECTION: {addr} connected...")
    connected = True
    while connected:
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            if msg == DISCONNECT:
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"SERVER IS LISTENING ON {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client, args=(conn,addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS: {threading.activeCount() - 1}\n")

print(f"SERVER {server_name} IS STARTING, PLEASE WAIT...")
start()
