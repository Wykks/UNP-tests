NO_INFO_STRING = '?'

def readResults(config):
    results = dict()
    with open(config['unpdir'] + '/unp_album_name.txt', encoding='utf-8') as text:
        results['albumName'] = text.read()
    with open(config['unpdir'] + '/unp_artist_name.txt', encoding='utf-8') as text:
        results['artistName'] = text.read()
    with open(config['unpdir'] + '/unp_duration.txt', encoding='utf-8') as text:
        results['duration'] = text.read()
    with open(config['unpdir'] + '/unp_now_playing.txt', encoding='utf-8') as text:
        results['nowPlaying'] = text.read()
    with open(config['unpdir'] + '/unp_track_name.txt', encoding='utf-8') as text:
        results['trackName'] = text.read()
    with open(config['unpdir'] + '/unp_url.txt', encoding='utf-8') as text:
        results['url'] = text.read()
    return results
