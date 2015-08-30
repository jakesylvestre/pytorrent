'''
Jake Sylvestre
Simple Bittorrent Client
Usage python main.py file.torrent
'''
import argparse
import pytorrent.data
import pytorrent.tracker

def main(filepath):
    data_retreive = pytorrent.data.get_data(filepath)
    tracker = pytorrent.tracker.tracker_connect(data_retreive)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download a torrent file, seed, and use DHT.')
    parser.add_argument('torrent', metavar='t', type= str, nargs='+', help='The torrent file you wish to download')
    args = parser.parse_args()
    torrent_file = args.torrent[0]
    main(torrent_file)
