import socket
from threading import Thread

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address='127.0.0.1'
port=8000

client.connection((ip_address, port))

print("connected with server...")

def recieve():
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message='{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

recieve_thread= Thread(target=recieve)
recieve.start()
write_thread=Thread(target=write)
write_thread.start