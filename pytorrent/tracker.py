import urllib #not sure if this is required yet
import requests
class tracker_connect():
    def __init__(self, data):
        self.data = data
        self.uploaded = 0
        self.downloaded = 0
        self.left = self.data.length

    def url_form(self, url, event, numwant=50):
        params = {
            'info_hash' : self.data.info_hash,
            'peer_id' : self.data.peer_id,
            'uploaded' : self.uploaded,
            'downloaded' :  self.downloaded,
            'left' : self.left,
            'event' : event,
            'ip' : self.data.IP,
            'numwant' : numwant,
            'key' : self.data.key
            }
        url = url +
