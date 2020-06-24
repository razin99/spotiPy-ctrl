from ahk import AHK
from spotify_local import SpotifyLocal

with SpotifyLocal() as s:
    pass
    print(s.get_current_status)