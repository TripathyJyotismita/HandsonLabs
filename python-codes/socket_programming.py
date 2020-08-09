import socket

ip= input('enter ip:')
port=input('enter port:')

socket_obj = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
con = socket.create_connection(ip, port)

data = con.recv(1024)
print(data)

#-----------------------------------------
import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")

socket.inet_aton()