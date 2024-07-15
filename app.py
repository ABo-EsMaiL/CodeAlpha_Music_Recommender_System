import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pickle

# Spotify API credentials
SPOTIPY_CLIENT_ID = '68706e4baec64b1fbd4e59157e43d9c1'
SPOTIPY_CLIENT_SECRET = '701bce07b28b45818fc2ec0afc9f1c06'

def init_spotify_client(client_id, client_secret):
    credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=credentials_manager)

def fetch_album_cover_url(spotify_client, song_name, artist_name):
    query = f"track:{song_name} artist:{artist_name}"
    results = spotify_client.search(q=query, type="track")
    if results and results["tracks"]["items"]:
        album_cover_url = results["tracks"]["items"][0]["album"]["images"][0]["url"]
        return album_cover_url
    return "https://i.postimg.cc/0QNxYz4V/social.png"

def load_data():
    music = pickle.load(open('data.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return music, similarity

def get_recommendations(music, similarity, song, spotify_client):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music = []
    for i in distances[1:6]:
        song_name = music.iloc[i[0]].song
        artist_name = music.iloc[i[0]].artist
        album_cover_url = fetch_album_cover_url(spotify_client, song_name, artist_name)
        recommended_music.append((song_name, artist_name, album_cover_url))
    return recommended_music

def display_recommendations(recommended_music):
    st.subheader("Recommended Songs")
    for i in range(0, len(recommended_music), 3):
        cols = st.columns(3)
        for idx, col in enumerate(cols):
            if i + idx < len(recommended_music):
                song_name, artist_name, album_cover_url = recommended_music[i + idx]
                with col:
                    st.write(f"**{song_name}** by {artist_name}")
                    st.image(album_cover_url, width=150)
                    st.markdown("---")

def main():
    st.title('Music Recommender System')

    # Load data
    music, similarity = load_data()
    music_list = music['song'].values

    # Spotify client
    spotify_client = init_spotify_client(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)

    # User input
    selected_song = st.selectbox("Select a song from the dropdown", music_list)

    if st.button('Show Recommendation'):
        with st.spinner('Fetching recommendations...'):
            recommended_music = get_recommendations(music, similarity, selected_song, spotify_client)
        display_recommendations(recommended_music)

if __name__ == "__main__":
    main()
