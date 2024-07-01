import streamlit as st
import pandas as pd

# Function to load custom CSS
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Function to load custom JS
def load_js(file_path):
    with open(file_path) as f:
        js = f.read()
    st.markdown(f'<script>{js}</script>', unsafe_allow_html=True)

# Load the custom CSS and JS
load_css("style.css")
load_js("main.js")

# HTML for the 3-D heading and main content
html_content = """
<div id="heading-3d" class="heading-3d">Music Recommendation System</div>
<div id="main-content" class="hidden">
    <h1>Music Recommendation System</h1>
    <div class="stForm">
        <label for="genres">Select your preferred genres:</label>
        <div id="genres">{}</div>
        <label for="energy">Select your current energy level:</label>
        <div id="energy">{}</div>
        <button id="submit" class="stButton">Submit</button>
    </div>
</div>
"""

# Load CSV files
data_by_artist = pd.read_csv('data_by_artist.csv')
data_by_genres = pd.read_csv('data_by_genres.csv')
data_by_year = pd.read_csv('data_by_year.csv')
data = pd.read_csv('data.csv')
data_w_genres = pd.read_csv('data_w_genres_updated.csv')  # Updated file

# Streamlit app
st.title("Music Recommendation System")

# User inputs
genres = st.multiselect('Select your preferred genres', options=data_by_genres['genres'].unique())
energy_level = st.slider('Select your current energy level', 0.0, 1.0, 0.5)

# Function to create YouTube search URL
def create_youtube_link(artist):
    base_url = "https://www.youtube.com/results?search_query="
    search_query = f"{artist.replace(' ', '+')}+songs"
    return base_url + search_query

# Filter data based on user inputs
if st.button('Submit'):
    if genres:
        # Filter data based on selected genres
        filtered_data = data_w_genres[data_w_genres['genres'].apply(lambda x: any(item in x for item in genres))]

        # Display available data based on user input
        st.write("Available Data Based on Your Selection:")
        if not filtered_data.empty:
            filtered_data_preview = filtered_data[['artists', 'genres', 'energy']].drop_duplicates()
            st.dataframe(filtered_data_preview)
        else:
            st.write("No data found for the selected genres.")

        # Ensure 'energy' is numeric
        filtered_data['energy'] = pd.to_numeric(filtered_data['energy'], errors='coerce')

        if 'energy' not in filtered_data.columns:
            st.write("The 'energy' column is missing in the data.")
        else:
            filtered_data = filtered_data.dropna(subset=['energy'])
            recommendations = filtered_data[filtered_data['energy'] >= energy_level]

            st.write("Recommended Songs:")
            if not recommendations.empty:
                recommendations = recommendations[['artists', 'genres']].drop_duplicates()

                for index, row in recommendations.iterrows():
                    artist = row['artists']
                    genre = row['genres']
                    youtube_link = create_youtube_link(artist)
                    st.markdown(f"- **{artist}** (Genre: {genre}) [Listen on YouTube]({youtube_link})", unsafe_allow_html=True)
            else:
                st.write("No recommendations found for the selected criteria.")
    else:
        st.write("Please select at least one genre.")
