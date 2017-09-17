import socket
import os
import threading

def Main():
    host = '127.0.0.1'
    port = 4444

    s = socket.socket()
    s.bind((host,port))

    s.listen(2)
    print("Server started...: " + host + " : "+str(port))

    try:
        while True:
            sock, addr = s.accept()
            print("Connection Established with IP: " + str(addr))
            t = threading.Thread(target=fetchFile, args=(sock,))
            t.start()
    except:
        s.close()
        
    
def fetchFile(sock):
    fileName = sock.recv(1024).decode('utf-8')
    if os.path.isfile(fileName):
        response = "OK. " + fileName + " exists. Size: " + str(os.path.getsize(fileName)) + ". Do you want to proceed with downloading? (y/n): "
        sock.send(response.encode('utf-8'))
        userResponse = sock.recv(1024).decode('utf-8')
        if userResponse in {'y','Y'}:
            with open(fileName, 'rb') as file:
                bytesToSend = file.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = file.read(1024)
                    sock.send(bytesToSend)
        else:
            sock.send(("You Chose not to download the file").encode('utf-8'))
            sock.close()

    else:
        response = "File does not exist. Try again.."
        sock.send(response.encode('utf-8'))

    sock.close()    

if __name__ == '__main__':
    Main()
