import requests
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

spotifyID = ""
spotifySecretKey = ""

year = input("What year would like to travel to in YYY-MM-DD format: ")

url = f"https://www.billboard.com/charts/hot-100/{year}"
response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")
title = soup.select("li ul li h3")
song_title = [song.getText().strip() for song in title]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=spotifyID,
        client_secret=spotifySecretKey,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
chosen_year = year.split("-")[0]

song_uris = []
for song in song_title:
    result = sp.search(q=f"track:{song} year:{chosen_year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass
playist_name = "Billoard to Spotify"
playlist = sp.user_playlist_create(user_id, name=f"{chosen_year} Billboard 100", public=False)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)
