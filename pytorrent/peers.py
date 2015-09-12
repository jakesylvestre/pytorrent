import twisted #TODO implement twisted
import socket
import pytorrent.network
#from network import network_info

class peer_connect:
    def __init__(self, peer, network_info, data):
        self.network = pytorrent.network.network_info()
        self.peer = peer
        self.address = self.peer[0]#todo fix
        self.port = self.peer[1]#todo fix
        self.data = self.init_handshake()
        print self.data

    def init_handshake(self):
    	""" Sends a handshake, returns the data we get back. """

    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	s.connect((self.peer))
    	s.send(handshake)

    	data = s.recv(len(handshake))
    	s.close()
    	return data

    def get_peer(self):
        return self.peer

    def get_adress(self):
        return self.address

    def get_port(self):
        return self.port
