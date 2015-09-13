import socket

class network_info:
    def __init__(self):
        self.ipv6 = socket.has_ipv6
        self.timeout = socket.getdefaulttimeout()
    def has_ipv6(self):
        return self.ipv6

    def get_timeout(self):
        return self.timeout
