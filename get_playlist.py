import requests
import json
def api_call(playlist, access_token):
    playlist_id = playlist.split('/')[-1] # https://open.spotify.com/playlist/3sMT03qQymfudj1Xl88GPK?si=qggszptlQTSCauZHlsGmVw
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})
    api_response = json.dumps(response.json(), indent=4)

    
    return api_response