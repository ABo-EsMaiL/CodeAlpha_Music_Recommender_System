# Music Recommender System

This project is a music recommender system that suggests songs based on the user's input using a dataset of Spotify songs.

## Dataset

The dataset used is `spotify_millsongdata.csv` which contains information about various songs on Spotify.

## Features

- Text preprocessing including stemming and removing special characters.
- TF-IDF vectorization of song lyrics.
- Cosine similarity to find similar songs.
- Streamlit app for an interactive user interface.
- Spotify API integration to fetch album cover images.

## Requirements

- Python 3
- Libraries:
  - numpy
  - pandas
  - nltk
  - seaborn
  - matplotlib
  - scikit-learn
  - streamlit
  - spotipy

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/ABo-EsMaiL/Music-Recommender-System.git
    cd Music-Recommender-System
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Download NLTK data:
    ```sh
    python -m nltk.downloader punkt
    ```

4. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Select a song from the dropdown menu in the Streamlit app.
2. Click on 'Show Recommendation' to get song recommendations.

## Author

- Ahmed AbdElHady Esmail

## License

This project is licensed under the MIT License.

## **`Using`**

![predict1](image.png)
![predict2](image-1.png)
![predict3](image-2.png)
![predoct4](image-3.png)
