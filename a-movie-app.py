# streamlit_app.py
import streamlit as st
import pandas as pd

# Load data
file_path = "movies.csv"  # Ensure this path matches the location of your CSV file in the repo
movies_df = pd.read_csv(file_path)

# App Title
st.title("IMDB Top Movies Exploration App")

# Sidebar Filters
st.sidebar.header("Filter Options")
year_filter = st.sidebar.slider("Select Year Range", int(movies_df['year'].min()), int(movies_df['year'].max()), (2000, 2020))
genre_filter = st.sidebar.multiselect("Select Genres", options=movies_df['genre'].unique())

# Filter Data
filtered_df = movies_df[
    (movies_df['year'] >= year_filter[0]) & 
    (movies_df['year'] <= year_filter[1])
]
if genre_filter:
    filtered_df = filtered_df[filtered_df['genre'].str.contains('|'.join(genre_filter), na=False)]

# Display Data
st.subheader("Filtered Movies")
st.dataframe(filtered_df)

# Display Movie Statistics
st.subheader("Movie Statistics")
st.write(f"Total Movies: {len(filtered_df)}")
st.write(f"Average Rating: {filtered_df['imbd_rating'].astype(float).mean():.2f}")

# Display Top Movie
st.subheader("Top Rated Movie")
top_movie = filtered_df.iloc[filtered_df['imbd_rating'].astype(float).idxmax()]
st.write(f"**{top_movie['title']}** ({top_movie['year']}) - {top_movie['imbd_rating']} ⭐")
st.write(top_movie['storyline'])

# Show a link to the movie on IMDB
st.markdown(f"[IMDB Link]({top_movie['link']})")
