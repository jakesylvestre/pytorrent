import twisted #TODO implement twisted 
import socket
#from network import network_info

class peer_connect:
    def __init__(self, peer, network_info):
        self.network = network_info
        self.peer = peer
        self.address = self.peer[0]
        self.port = self.peer[1]

    
    def connect_to_peer(self):
        self.connection = socket.create_connection(peer, network.get_timout())
        return self.connection
        
    def get_peer(self):
        return self.peer
    
    def get_adress(self):
        return self.address
    
    def get_port(self):
        return self.port