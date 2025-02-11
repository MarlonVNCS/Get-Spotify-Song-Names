import json
def get_tracks(response):
    data = json.loads(response)['tracks']['items']
    tracks = []
    for track in data:
        tracks.append(f"{track['track']['artists'][0]['name']} - {track['track']['name']}")
    
    return tracks