import socket
import re

def Main():
    host = '127.0.0.1'
    port = 4444
    
    s = socket.socket()
    s.connect((host,port))

    while True:
        fileName = input("[+] Enter q to quit or Enter Filename: ")
        if(fileName != 'q'):
            s.sendall(fileName.encode('utf-8'))

            serverResponse = s.recv(1024).decode('utf-8')
            print('[!] '+serverResponse)
                
            if(serverResponse[:2] == 'OK'):
                regEx = re.compile(r'Size: [0-9]*')
                size = regEx.findall(serverResponse)
                print(size)
                fileSize = int(size[0].replace('Size: ',''))
                confirm = input("(y/n) >>> ")
                s.sendall(confirm[0].encode('utf-8'))

                if confirm[0] in {'y','Y'}:
                    file = open("downloaded_"+fileName, 'wb')
                    data = s.recv(fileSize)
                    #totalRecv = len(data)
                    file.write(data)

                    '''while(totalRecv <= fileSize):
                        data = s.recv(1024)
                        totalRecv += len(data)
                        file.write(data)'''

                    print("[+] Download Complete!")
                    file.close()

        else:
            s.close()
            exit(0)
    s.close()
    exit(0)

if __name__ == "__main__":
    Main()
        
