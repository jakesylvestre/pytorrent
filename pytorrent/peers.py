from twisted.internet import reactor #TODO implement twisted
import socket
import pytorrent.network as network
#from network import network_info

class peer_connect:
    def __init__(self, peer, data):
        self.data = data
        self.network = pytorrent.network.network_info()  #TODO all this crap gets inherited from connect to peers
        self.peer = peer
        self.address = self.peer[0]
        self.port = self.peer[1]
        self.datas = self.send_handshake()
        print "handshake is " + str(type(self.datas))
        print str(self.datas)
        print self.datas
    def send_handshake(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self.peer)
        s.send(self.data.handshake)

        data = s.recv(4696) #TODO after testing revert to: len(self.data.handshake
        s.close()

        return data

    def get_peer(self):
        return self.peer

    def get_adress(self):
        return self.address

    def get_port(self):
        return self.port

class connect_to_peers:
    def __init__(self, peers, data):
            from twisted.internet import reactor
            self.data = data
            self.network = network
            self.peers = peers
    def handshake(self):
        peer = ()
        print self.peers[1]
        for data in self.peers:
            if len(peer) == 0:
                peer = (data, )
                self.peers.pop(0)
                continue
            elif len(peer) == 1:
                peer = peer + (data, )
                self.peers.pop(0)
                continue
            elif len(peer) == 2:
                print "ip is " + peer[0]
                print "peer is " + peer[1] 
                reactor.connectTCP(self.peers[0], self.peers[1], network.peer())
                peer = ()
