from twisted.internet.protocol import Protocol, ClientFactory


class Received(Protocol): #TODO add constructors
    output = ""

    def dataReceived(self, data):
        output += data
        if len(output) == 9:
            #somehow close the connection
            return output
class peer(ClientFactory):
    def startedConnecting(self, connector):
        pass

    def buildProtocol(self, addr):
        print 'Connected.'
        print 'Resetting reconnection delay'
        #self.resetDelay()
        return Received() #Start receiving data

    def clientConnectionLost(self, connector, reason):
        pass
        #print 'Lost connectiom.  Reason:', reason
        #ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        pass
        #print 'Connection failed. Reason:', reason
        #ReconnectingClientFactory.clientConnectionFailed(self, connector,
