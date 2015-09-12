import twisted #TODO implement twisted
import socket
import pytorrent.network
#from network import network_info

class peer_connect:
    def __init__(self, peer, network_info, data):
        self.data = data
        self.network = pytorrent.network.network_info()
        self.peer = peer
        self.address = self.peer[0]
        self.port = self.peer[1]
        print "handshake is " + type(self.send_handshake())
        
    def send_handshake(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self.peer)
        s.send(self.data.handshake)

        data = s.recv(len(self.data.handshake))
        s.close()

        return data

    def get_peer(self):
        return self.peer

    def get_adress(self):
        return self.address

    def get_port(self):
        return self.port
