#Jarett Sutula
#9.16.19

#create an open socket server in python
#use cURLs, can use TCP, port 1337

from siop import *
import socket
import pprint

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 1337
HOST = '127.0.0.1'

#let's bind it to the host and port.
s.bind((HOST,PORT))
#let's open it
s.listen(5)
obj = Message()

def parse(data):
    for line in data.splitlines():
        if line.find(":") != -1 :
            key, value = line.split(":",1)
            setattr(obj, key, value)
    return(obj)

while True:
    #open a connection
    conn,addr = s.accept()
    fullData = ''

    #print that we are connected w/ address.
    print('Connected by', addr)
    while True:
        #recieve 10 bytes
        data = conn.recv(10)

        #convert data to a string.
        data = str(data.decode("utf-8"))

        #if the data is empty, break it
        if data == '':
            break

        #data isn't full - add the data together
        else:
            fullData = fullData + data

        #let's send something back to console
        #something here to print/return

        packet = parse(fullData)
        pprint.pprint(vars(obj))
        #if (packet['value'] == "BREAK"):
        #    break
