import socket

class network_info:
    def __init__(self):
        self.ipv6 = socket.has_ipv6
        self.tiemout = socket.getdefaulttimeout()
    def has_ipv6(self):
        return self.ipv6
