import unittest
import urllib
import os
import bencode
from pytorrent import data
import datetime
import ipgetter

#TODO fix: https://gist.github.com/jakesyl/20a7e0b8d040caf58684

class error(Exception):
    def __init__(self, err):
        Exception.__init__(self)
        self.err = err
    def __str__(self):
        return repr(self.err)

class get_test_file():
    def __init__(self):
        self.CUR_DIR = os.getcwd()
        test_file = "test.torrent"
        test_file = self.CUR_DIR + "/pytorrent/tests/" + test_file
        if os.path.isfile(test_file):
            self.test_file = test_file
        else:
            err_handle= error("Error!")



class TestGetData(unittest.TestCase):

    def test_trackers(self):
        test_file = get_test_file()
        self.test_file = test_file.test_file
        test_data = data.get_data(self.test_file)
        self.assertEqual(test_data.get_trackers(),[['http://torrent.ubuntu.com:6969/announce'], ['http://ipv6.torrent.ubuntu.com:6969/announce']])
        self.assertEqual(test_data.get_trackers(), test_data.trackers)
    def test_info_hash(self):
        test_file = get_test_file()
        self.test_file = test_file.test_file
        test_data = data.get_data(self.test_file)
        self.assertEqual(test_data.get_info_hash(), 'fc8a15a2faf2734dbb1dc5f7afdc5c9beaeb1f59')
        self.assertEqual(test_data.get_info_hash(), test_data.info_hash)
    def test_get_length(self):
        test_file = get_test_file()
        self.test_file = test_file.test_file
        test_data = data.get_data(self.test_file)
        self.assertEqual(test_data.get_length(), 1150844928)
        self.assertEqual(test_data.get_length(), test_data.length)
        self.assertEqual(test_data.length, test_data.left)
    def test_creation_date(self):
        test_file = get_test_file()
        self.test_file = test_file.test_file
        test_data = data.get_data(self.test_file)
        self.assertEqual(test_data.get_creation_date(), test_data.creation_date)
    def test_ip(self):
        test_file = get_test_file()
        self.test_file = test_file.test_file
        test_data = data.get_data(self.test_file)
        self.assertEqual(ipgetter.myip(), test_data.IP)
    def test_peer_id(self):
        test_file = get_test_file()
        self.test_file = test_file.test_file
        test_data = data.get_data(self.test_file)
        self.assertEqual(20, len(test_data.gen_peer_id()))
if __name__ == '__main__':
    unittest.main()
