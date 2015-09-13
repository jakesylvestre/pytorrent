import bencode
import hashlib
from random import choice
import StringIO
from datetime import datetime
import ipgetter
import os
from random import randint
import socket
import struct
class get_data():
    def __init__(self, filepath):
        print a
        self.filepath = filepath
        torrent_file = ''
        self.file =  open(self.filepath, 'rb')
        for line in self.file:
            torrent_file += line #not bounded by system memory/size of file
        self.file.close()
        self.torrent_file = bencode.bdecode(torrent_file)
        self.ID = "PT"
        self.VERSION = "0000"
        self.RESERVED = "00000000"
        self.PROTOCOL = "BitTorrent protocol"
        self.trackers = self.get_trackers()
        self.info_hash = self.get_info_hash()
        self.peer_id = self.gen_peer_id()
        self.length = self.get_length()
        self.left = self.length#TODO remove this and pertinent unit tests
        self.creation_date = self.get_creation_date()
        self.IP = ipgetter.myip()
        self.key = self.get_key()
        self.info_hash_hex = self.get_info_hash_hex()
        self.port = self.get_port()
        self.handshake = self.get_handshake()
        self.ipv6 = socket.has_ipv6
        self.timeout = socket.getdefaulttimeout()
    def get_info_hash(self):
        '''
        Jake Sylvestre
        generate the info_hash based on the info section
        '''
        return hashlib.sha1(bencode.bencode(self.torrent_file['info'])).hexdigest()
    def get_info_hash_hex(self):
        return hashlib.sha1(bencode.bencode(self.torrent_file['info'])).digest()

    def get_trackers(self):
            return self.torrent_file['announce-list']

    def gen_peer_id(self):
        #TODO if you get blocked, spoof https://wiki.theory.org/BitTorrentSpecification#peer_id
        #Azures is more popular than shadow
        random_string = ""
        while len(random_string) != 12:
            random_string += choice("1234567890")
        return "-" + self.ID + self.VERSION + "-" + random_string

    def get_length(self):
        length = 0
        try:
            for piece in self.torrent_file['info']['files']:
                length += piece['length']
        except KeyError:
            length = self.torrent_file['info']['length']
        return length
    def get_creation_date(self):
        date = self.torrent_file['creation date']
        date = datetime.fromtimestamp(date)
        return date
    def get_key(self):

        try:
            return os.urandom(20)
        except NotImplementedError:
            from random import randint
            return str(randint(10000000000000000000, 99999999999999999999))
    def get_port(self):
        for port in range(6881, 6889):
            try:
                result = socket.socket.connect_ex(('127.0.0.1', port))
                if result==0:
                    return port
                else:
                    continue
            except AttributeError as e:
                print e
                return port
            except TypeError as e:
                print e
                return port
            except:
                print "ERROR returning " + str(port)
                return port
    def get_handshake(self):
        return str(len(self.PROTOCOL)) + self.PROTOCOL + self.RESERVED + self.info_hash_hex + self.peer_id


        #return str(randint(10000000000000000000, 99999999999999999999))
class get_peer_data():
    def __init__(self, bcode):
        self.peer_data = bencode.bdecode(bcode)#todo convert from binary
        self.peers = self.peer_data["peers"]
        final_peers = []
        for peer in xrange(0, len(self.peers), 6):
            ip, port = struct.unpack('!4sH', self.peers[peer:peer+6])
            ip = socket.inet_ntop(socket.AF_INET, ip)
            host = (ip, port)
            final_peers += host
        self.peers = final_peers
        #self.peers = self.peers.decode()    family = sa.sa_family


    def get_interval(self):
        return self.peer_data["interval"]

    def get_complete(self):
        return self.peer_data["complete"]

    def get_incomplete(self):
        return self.peer_data["incomplete"]

    def get_peers(self):
        return self.peers
