import socket
from getmac import get_mac_address as gma

HEADER = 64
PORT = 3074
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
SERVER = "158.251.91.68"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def auth(mac):
    mad = mac.enconde(FORMAT)
    madlen = '17'.encode(FORMAT)+b' '*47
    client.send(madlen)
    client.send(mad)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


auth(gma())

input()
send("Hello")
input()
send("I made it!")
input()
send("Bye")

send(DISCONNECT_MESSAGE)