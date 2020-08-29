import socket,select, sys,time

class Broadcaster:

    def execute(self):
        addr = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.bind((addr, 1235))
        s.settimeout(0.3)
        message = b'Hello'
        while True:

            s.sendto(message, ('<broadcast>', 3000))
            try:
                recvmessage, address = s.recvfrom(1024)
                ip = address[0]
                print "Got data from", address , ' tcp server is ready on port :', recvmessage
                tcpPort = recvmessage
                s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s2.connect((ip, int(tcpPort)))
                s2.send("chat initiation")
                data2 = s2.recv(1024)

                print '(TCP server) : ', data2

                while True:

                    message = raw_input()
                    s2.send(message)
                    if "bye" in message:
                        print '\nthis connection closed'
                        break
                    data2 = s2.recv(1024)
                    print data2
                    if "bye" in data2:
                        print 'connection with server closed :('
                        break
            except socket.timeout:
                time.sleep(2)
















