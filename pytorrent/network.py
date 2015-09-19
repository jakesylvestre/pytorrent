from twisted.internet.protocol import Protocol, ClientFactory



class Received(Protocol): #TODO add constructors
    output = ""
    def __init__(self, handshake):
        self.handshake = handshake
        self.expected = len(self.handshake)
    def dataReceived(self, data):
        output += data
        if len(output) == self.expected:
            #somehow close the connection
	    print output
            return output
    def connectionMade(self):
        pass
        #self.transport.write(handshake)

class peer(ClientFactory):
    def __init__(self, handshake):
        self.handshake = handshake

    def startedConnecting(self, connector):
        pass

    def buildProtocol(self, addr):
        print 'Connected.'
        #self.resetDelay()
        return Received(handshake) #Start receiving data

    def clientConnectionLost(self, connector, reason):
        pass
        #print 'Lost connectiom.  Reason:', reason
        #ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        pass
        #print 'Connection failed. Reason:', reason
        #ReconnectingClientFactory.clientConnectionFailed(self, connector,

