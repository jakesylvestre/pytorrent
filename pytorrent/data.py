import bencode
import hashlib
from random import choice
import StringIO
from datetime import datetime

class get_data(): #TODO write unit tests
    def __init__(self, filepath):
        self.filepath = filepath
        torrent_file = ''
        self.file =  open(self.filepath, 'rb')
        for line in self.file:
            torrent_file += line #not bounded by system memory/size of file
        self.file.close()
        self.torrent_file = bencode.bdecode(torrent_file)
        self.ID = "PT"
        self.VERSION = "0000"
        self.trackers = self.get_trackers()
        self.info_hash = self.get_info_hash()
        self.peer_id = self.gen_peer_id()
        self.length = self.get_length()
        self.left = self.length
        self.creation_date = self.get_creation_date()

    def get_info_hash(self):
        return hashlib.sha1(bencode.bencode(self.torrent_file['info'])).hexdigest()

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
