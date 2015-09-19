from twisted.internet.protocol import Protocol, ClientFactory



class Received(Protocol): #TODO add constructors
    output = ""
    def __init__(self, handshake):
        self.handshake = handshake
        self.expected = len(self.handshake)
    def dataReceived(self, data):
        output += data
        print "data is " + data
        if len(output) == self.expected:
            #somehow close the connection
	    print "output is " + output
            return output
    def connectionMade(self):
        self.transport.write(self.handshake)

class peer(ClientFactory):
    def __init__(self, handshake):
        self.handshake = handshake

    def startedConnecting(self, connector):
        print "started connecting  "

    def buildProtocol(self, addr):
        print 'Connected.'
        #self.resetDelay()
        return Received(self.handshake) #Start receiving data

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason
        #ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason
        #ReconnectingClientFactory.clientConnectionFailed(self, connector,

