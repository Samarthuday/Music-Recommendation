

# Music Recommendation System Using Spotify Dataset

## Overview

The purpose of this project is to develop a robust music recommendation system leveraging data from Spotify. By integrating with Spotify's API and utilizing advanced data analysis techniques, the system aims to provide personalized song recommendations based on user input and listening preferences. The system utilizes multiple datasets encompassing various parameters such as genre, tempo, popularity, danceability, acousticness, energy, instrumentalness, liveness, speechiness, and valence. These datasets enhance the accuracy and relevance of recommendations, ensuring an engaging user experience.

## Features

The key features of your recommendation system:
- Recommendation based on user preferences
- Integration with Spotify API

## Installation

Instructions on how to install and set up your project:
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the frontend directory: `cd frontend`
3. Install frontend dependencies: `npm install`
4. Set up Spotify API credentials:
   - Create a Spotify developer account and register your application.
   - Obtain Client ID and Client Secret.
   - Update configuration file (`config.js`) with these credentials.

## Usage

Explain how to use your recommendation system:
1. Start the frontend server: `npm start`
2. Open the application in your web browser at `http://localhost:3000`
3. Log in with your Spotify account.
4. Explore recommended music based on your listening history.

## Dataset

1.data_by_artist:
- Description: Provides aggregated audio features of tracks by artist.
- Parameters: Includes metrics such as danceability, energy, loudness, and more.
- Purpose: Enables artist-centric recommendations and analysis of artist-specific music characteristics.

2.data_by_genres:
- Description: Contains aggregated audio features of tracks by genre.
- Parameters: Includes genre-specific metrics like acousticness, instrumentalness, and popularity.
- Purpose: Facilitates genre-based recommendations and genre-specific insights into music preferences.

3.data_by_year:
- Description: Provides audio features of tracks aggregated by year.
- Parameters: Includes temporal metrics such as tempo, valence, and duration.
- Purpose: Analyzes music trends over time and facilitates historical music exploration based on year of release.

4.data_w_genres:
- Description: Includes audio features of tracks with genre labels.
- Parameters: Combines track-specific metrics with genre categorization.
- Purpose: Enhances genre-based and track-specific recommendations, incorporating genre classification into song analysis.

5.data:
- Description: Comprehensive dataset containing audio features of tracks.
- Parameters: Includes a wide range of metrics such as speechiness, liveness, and instrumentalness.
- Purpose: Forms the foundational dataset for detailed song analysis and personalized recommendations based on diverse music attributes.
  

These datasets are integral to the recommendation algorithm, leveraging Spotify's extensive music library and API for real-time data retrieval and analysis. By combining these diverse datasets, the system ensures that users receive highly personalized music recommendations aligned with their unique listening preferences and habits.

## Technologies Used

The main technologies and libraries used in your project:
- React
- Spotify API
- Node.js 
- Express
- Pandas


