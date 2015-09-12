import twisted #TODO implement twisted
import socket
import pytorrent.network
#from network import network_info

class peer_connect:
    def __init__(self, peer, network_info):
        self.network = pytorrent.network.network_info()
        self.peer = peer
        self.address = self.peer[0]
        self.port = self.peer[1]

    def init_connection(self):
        print (self.peer)
        self.connection = socket.create_connection(self.peer)
        print "connection to " + str(self.connection)
        return self.connection

    def get_peer(self):
        return self.peer

    def get_adress(self):
        return self.address

    def get_port(self):
        return self.port
