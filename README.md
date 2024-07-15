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
    git clone https://github.com/ABo-EsMaiL/CodeAlpha_Music_Recommender_System.git
    cd CodeAlpha_Music_Recommender_System
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

![image](https://github.com/user-attachments/assets/33ee244d-498e-46b4-b65f-7b764b30bc99)
![image-1](https://github.com/user-attachments/assets/35813b66-1714-42c6-9da4-ee37b630f1ae)
![image-2](https://github.com/user-attachments/assets/bed25f42-4b72-4a44-8426-df70b62f7889)
![image-3](https://github.com/user-attachments/assets/25a0d54d-5767-459f-8766-f2a8e49539b2)
