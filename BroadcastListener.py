import socket, random, select, sys

class BroadcastListener():
    def execute(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', 3000))
        while True:

            data, addr = s.recvfrom(1024)  # type: (str, object)
            print(data)
            print 'Got invitation from broadcaster :  ', addr
            portNum = random.randint(49152, 65535)
            print "I'm ready on port :  ", portNum
            s.sendto(str(portNum), addr)
            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2.bind(('', portNum))
            s2.listen(1)
            while True:
                conn, addr2 = s2.accept()
                print 'Connected by :  ', addr2
                firstdata = conn.recv(1024)
                print addr2, ' :  ', firstdata
                conn.sendall("Let's chat")
                while True:
                    data = conn.recv(1024)
                    print addr2, ':', data
                    if "bye" in data:
                        print 'connection with ', addr2, ' closed :('
                        break
                    # if len(data) == 0:
                    #    break
                    message = raw_input()
                    conn.sendall('server :  ' + message)

                s2.close








