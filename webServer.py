#import socket module
from socket import *

# Setting up server socket
server_socket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket (binding and listening for incoming connections) and provide port number 
server_socket.bind(('', 6789))
server_socket.listen(1)

print('Ready to serve...')

while True:
    #accepts the connection
    connectionSocket, addr = server_socket.accept()
    
    #starts the process of reading the file
    message = connectionSocket.recv(1024).decode()
    
    try:
        #extracts the file 
        filename = message.split()[1]

        #opens the file 
        f = open(filename[1:], "rb")

        #Send HTTP status/header line into socket
        connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n', 'utf-8'))

        outputdata = f.read()

        #Send the content of the requested file to the client (Web browser)
        while len(outputdata)>0:

            connectionSocket.send(outputdata)
            outputdata = f.read(1024)

        connectionSocket.close()

        #closes the file 
        f.close()

    #this response message is initialize through the command/code for the HTTP message of not finding the file specified
    except Exception as e:
        errorMess = b'HTTP/1.1 404 Not Found\r\n\r\n404 Not Found'
        connectionSocket.send(errorMess)
            
    #Close client socket
    connectionSocket.close()

# 1. Run sever --> python webServer.py
# 2. Open web broswer and type --> http://localhost:6789/HelloWorld.html
# File Not Found Tests --> http://localhost:6789/HelloBro.html
# or..                 --> http://localhost:6789