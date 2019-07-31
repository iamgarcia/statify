import spotipy
from spotipy import util

def get_songs(token):
    sp = spotipy.Spotify(auth=token)
    top_tracks = sp.current_user_top_tracks(limit=50, time_range='short_term')
    for item in top_tracks['items']:
        song_length = sp.track(item['uri'][-22:])['duration_ms']
        song_length = round(song_length/60000, 2)
        songs = {'name': item['name'], 'artists': item['artists'][0]['name'], 'album_title': item['album']['name'], 'song_length': song_length}
    return songs

token = util.prompt_for_user_token('jawe;ofji', 'user-top-read', client_id='d1043c275ddc4f64a60b2438db8ef839', client_secret='fe8389b1944e44199785a6607fc68da4', redirect_uri='https://new-statify-app.appspot.com/')
artists = []
songs = []

# {song tit: , artist:, album tit:, song time: }

if token:
    sp = spotipy.Spotify(auth=token)
    top_artists = sp.current_user_top_artists(limit=50, time_range='short_term')
    top_tracks = sp.current_user_top_tracks(limit=50, time_range='short_term')
    print('favorite artists')
    for item in top_artists['items']:
        print(item['name'])
    print('top tracks')
    for item in top_tracks['items']:
        song_length = sp.track(item['uri'][-22:])['duration_ms']
        song_length = round(song_length/60000, 2)
        songs = {'name': item['name'], 'artists': item['artists'][0]['name'], 'album_title': item['album']['name'], 'song_length': song_length}
        print(songs)
else:
    print("can't get token for user")