import streamlit as st
import numpy as np
import pickle
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
client_id = 'c252f68991f44d91ae2f845edcb5248e'
client_secret = '73cbed64b355457998bbed00ead38ebe'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Load data
music_dict = pickle.load(open("musicrec.pkl", 'rb'))
music = pd.DataFrame(music_dict)
similarity = pickle.load(open("similarities.pkl", 'rb'))
similarity = np.array(similarity)

# Fetch poster, Spotify link, and artist name
def fetch_poster_and_link(music_title):
    try:
        results = sp.search(q=music_title, limit=1, type='track')
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            poster_url = track['album']['images'][0]['url']
            spotify_url = track['external_urls']['spotify']
            artist = track['artists'][0]['name']
            return poster_url, spotify_url, artist
    except Exception as e:
        st.error(f"Error fetching poster or link for {music_title}: {e}")
    return "default_image_url", "#", "Unknown"

# Recommend function
def recommend(musics):
    try:
        music_index = music[music['title'] == musics].index[0]
        distances = similarity[music_index]
        music_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommendations = []
        for i, score in music_indices:
            music_title = music.iloc[i].title
            poster_url, spotify_url, artist = fetch_poster_and_link(music_title)
            recommendations.append({
                'title': music_title,
                'poster': poster_url,
                'link': spotify_url,
                'artist': artist
            })
        return recommendations
    except Exception as e:
        st.error(f"Error during recommendation: {e}")
        return []

# Streamlit UI
st.set_page_config(page_title="Music Recommendation System", layout="wide")
st.title('Music Recommendation System')

selected_music_name = st.selectbox('Select a music you like', music['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_music_name)

    if recommendations:
        for rec in recommendations:
            st.markdown(
                f"""
                <div style='display: flex; align-items: center; margin: 20px 0; background-color: #f9f9f9; padding: 15px; border-radius: 10px;'>
                    <div style='flex: 0 0 200px;'>
                        <img src="{rec['poster']}" width="180" style="border-radius: 10px;">
                    </div>
                    <div style='flex: 1; padding-left: 20px;'>
                        <h4 style='margin: 0; color: #333;'>{rec['title']}</h4>
                        <p style='margin: 5px 0; color: #666;'>Artist: {rec['artist']}</p>
                        <a href="{rec['link']}" target="_blank" style="text-decoration: none; color: #1DB954; font-weight: bold;">
                            Listen on Spotify
                        </a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.warning("No recommendations available for the selected song.")