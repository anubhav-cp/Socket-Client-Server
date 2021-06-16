import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'ascii'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))
server.listen()


clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receive():

    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")

        client.send('WEB'.encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the Chat!".encode(FORMAT))
        client.send("Connected to the Server!".encode(FORMAT))

        thread = threading.Thread(target = handle_client, args = (client,))
        thread.start()



print("[STARTING] Starting the Server...")
receive()

