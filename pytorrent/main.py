'''
Jake Sylvestre
Simple Bittorrent Client
Usage python main.py file.torrent
'''
import argparse
import pytorrent.data
import pytorrent.tracker
import pytorrent.network
import pytorrent.peers

def main(filepath):
    data_retreive = pytorrent.data.get_data(filepath)
    tracker = pytorrent.tracker.tracker_connect(data_retreive)
    peers = pytorrent.data.get_peer_data(tracker.fetch_peers())
    peers = peers.get_peers()
    print type(peers)
    network =  pytorrent.network.network_info()
    #TODO add networking
    peer = pytorrent.peers.peer_connect(peers[0], network)
    peer.init_connection()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download a torrent file, seed, and use DHT.')
    parser.add_argument('torrent', metavar='t', type= str, nargs='+', help='The torrent file you wish to download')
    args = parser.parse_args()
    torrent_file = args.torrent[0]
    main(torrent_file)
