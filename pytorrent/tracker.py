import requests

class tracker_connect():#TODO write unit test
    def __init__(self, data):
        self.data = data
        self.uploaded = 0
        self.downloaded = 0
        self.bad_trackers= list()
        self.left = self.data.length
        self.announce = self.find_http_announce_url()

    def find_http_announce_url(self):
        if self.is_http_url(self.data.torrent_file['announce']):
            return self.data.torrent_file['announce']
        elif 'announce-list' in self.data.torrent_file.keys():
            for url in self.data.torrent_file['announce-list']:
                url = url[0]
                if self.is_http_url(url):
                    if url not in self.bad_trackers:
                        return url
        raise SystemExit('UDP announce urls are not supported. Currently only HTTP is supported.')

    def is_http_url(self, url):
        return 'http://' in url


    def url_form(self, event, numwant=50):
        '''
        Jake Sylvestre
        form the url of the request: https://wiki.theory.org/BitTorrentSpecification#Tracker_Request_Parameters
        '''
        paramaters = {
            'info_hash' : self.data.info_hash_hex,
            'peer_id' : self.data.peer_id,
            'uploaded' : self.int_to_base_10(self.uploaded),
            'downloaded' :  self.int_to_base_10(self.downloaded),
            'left' : self.int_to_base_10(self.left),
            'event' : event,
            'ip' : self.data.IP,
            'numwant' : numwant,
            'key' : self.data.key,
            'compact' : 1,
            'port': 6881
            }
        return paramaters

    def int_to_base_10(self, num):
        return str(num)

    def fetch_peers(self, return_type="binary"):
        paramaters = self.url_form('started')
        r = requests.get(self.announce, params=paramaters)
        if ("d14:failure" in r.text) or ("your client is outdated, please upgrade" in r.text):# TODO add errors
            self.bad_trackers.append(self.announce)
            self.announce = self.find_http_announce_url()
            self.url_form(self.announce, 'started')
        else:
            if return_type == "binary":
                return r.content
            elif return_type == "text":
                return r.text
