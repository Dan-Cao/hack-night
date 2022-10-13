import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import config

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    redirect_uri="http://localhost/"
))

user_id = "38uwi63huv7sicy3b2dx954nw"
playlist = sp.user_playlist_create(user=user_id, name=f"my playlist {datetime.datetime.now().isoformat()}")
print("steve", playlist)
playlist_id = playlist["id"]

query = "dan"
search = sp.search(q=query, limit=50)
songs = search["tracks"]["items"]
print([(n["name"], n["duration_ms"]) for n in songs])

total_duration_ms = 0
target_duration_ms = 60 * 60 * 1000

songs_to_add = []

for song in sorted(songs, key=lambda x: x["duration_ms"], reverse=False):
    if total_duration_ms >= target_duration_ms:
        break

    songs_to_add.append(song["id"])
    total_duration_ms += song["duration_ms"]

result = sp.playlist_add_items(playlist_id=playlist_id, items=songs_to_add)
print(result)

print(
    f"target {target_duration_ms}, actual {total_duration_ms}, "
    f"diff {total_duration_ms - target_duration_ms}, num of songs {len(songs_to_add)}"
)
