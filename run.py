import create_token
import get_playlist
import get_tracks

# Spotify API Client ID
client_id = 'YOUR SPOTIFY API CLIENT ID'
# Spotify API Client Secret
client_secret = 'YOUR SPOTIFY API CLIENT SECRET'

# Get an access token from the Spotify API
token_type, access_token = create_token.get_token(client_id, client_secret)

# Spotify playlist URL
playlist = 'YOUR PLAYLIST URL'

# Call the Spotify API using a URL endpoint and an access token to retrieve data in JSON format
api_response = get_playlist.api_call(playlist, access_token)

# Extract track names and artists from a JSON object returned by the Spotify API
track_names = get_tracks.get_tracks(api_response)
print(track_names)