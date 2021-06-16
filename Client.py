import socket
import threading

PORT = 5050
FORMAT = 'ascii'
SERVER = socket.gethostbyname(socket.gethostname())

nickname = input("Enter Username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def write():
    run = True
    while run:
        msg = f"{nickname}: {input('')}"
        if msg == "quit":
            break
        message = msg.encode(FORMAT)
        client.send(message)


def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'WEB':
                client.send(nickname.encode(FORMAT))
            else:
                print(message)

        except:
            print("An Error Occured")
            client.close()
            break

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()



