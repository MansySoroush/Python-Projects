from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint

URL = "https://www.billboard.com/charts/hot-100/"

# Find your CLIENT_ID & CLIENT_SECRET at following Url
# and set it as environment variable.
SPOTIFY_END_POINT = "https://api.spotify.com/v1"

SPOTIFY_CLIENT_ID = "XXXX"
SPOTIFY_CLIENT_SECRET = "YYYY"

SPOTIFY_BASE_ARTIST_URI = "spotify:artist:"
REZA_BAHRAM_ID = "3DqvN5TEPxTPkaEN2N0HZ4"

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
user_date.strip()


def get_spotify_user_id() -> str:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Mansoureh"))

    return sp.current_user()["id"]


song_names = []
song_uris = []


def get_100_hot_song():
    date_url = URL + user_date

    # Scraping the Billboard Hot 100
    response = requests.get(date_url)
    billboard_hot_100 = response.text
    soup = BeautifulSoup(billboard_hot_100, "html.parser")

    global song_names
    song_names = [title.getText().strip() for title in soup.select("li ul li h3")]


def get_song_uris():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                               client_secret=SPOTIFY_CLIENT_SECRET))

    year = user_date.split("-")[0]
    for song_name in song_names:
        result = sp.search(q=f"track:{song_name} year:{year}", type="track")
        # print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song_name} doesn't exist in Spotify. Skipped.")


def create_billboard_tops_playlist_in_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Mansoureh"))

    user_id = sp.current_user()["id"]

    play_list_name = f"{user_date} Billboard 100"
    try:
        play_list = sp.user_playlist_create(user=user_id, name=play_list_name, public=False)
        play_list_id = play_list["id"]
        sp.playlist_add_items(playlist_id=play_list_id, items=song_uris)
        print("Done")
    except:
        print("ERROR")


get_100_hot_song()
get_song_uris()

pprint.pp(song_uris)

create_billboard_tops_playlist_in_spotify()
