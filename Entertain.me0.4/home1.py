import streamlit as st
from PIL import Image
import json
from bs4 import BeautifulSoup
import requests
import io
import PIL.Image
from urllib.request import urlopen
import ssl
from Classifier import KNearestNeighbours

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Define the app function
def app():
    
    st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    text-align: center;
}
.footer a {
    color: #333;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)
    st.markdown('<div class="footer"><a href="https://www.nclanarkshire.ac.uk">NCL HNC NextGen © 2024</a></div>', unsafe_allow_html=True)

    # Disable SSL certificate verification
    ssl._create_default_https_context = ssl._create_unverified_context
    # Define the category variable
    category = ['Select', 'Movie based', 'Genre based']

    # Load data and movie titles
    with open('./data/movie_data.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
    with open('./data/movie_titles.json', 'r+', encoding='utf-8') as f:
        movie_titles = json.load(f)
    hdr = {'User-Agent': 'Mozilla/5.0'}

    def movie_poster_fetcher(imdb_link):
        # Send a GET request to the IMDb link
        response = requests.get(imdb_link, headers=hdr)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the meta tag containing the poster link
            poster_meta_tag = soup.find("meta", property="og:image")
            
            # Check if the meta tag was found
            if poster_meta_tag:
                # Extract the content attribute (poster link) from the meta tag
                poster_link = poster_meta_tag.get('content')
                
                # Check if the poster link exists
                if poster_link:
                    # Fetch the poster image
                    try:
                        u = urlopen(poster_link)
                        raw_data = u.read()
                        image = PIL.Image.open(io.BytesIO(raw_data))
                        image = image.resize((350, 520))  # Make the poster bigger
                        st.image(image, use_column_width=False)  # Display the poster image
                    except Exception as e:
                        st.error("An error occurred while fetching the poster image.")
                        st.error(str(e))
                else:
                    st.error("Poster link not found.")
            else:
                st.error("Meta tag for poster image not found.")
        else:
            st.error("Failed to fetch IMDb page. Status code: " + str(response.status_code))
            
            
    def get_movie_info(imdb_link):
        url_data = requests.get(imdb_link, headers=hdr).text
        s_data = BeautifulSoup(url_data, 'html.parser')
    
    # Fetching story
        story_tag = s_data.find("meta", attrs={"name": "description"})
    
        if story_tag:
            movie_story = story_tag.attrs.get('content', 'Story information not available')
        else:
            movie_story = 'Story information not available'
    
    # Fetching rating
        rating_tag = s_data.find("span", class_="rating")
        movie_rating = rating_tag.text.strip() if rating_tag else "Rating information not available"
    
        return movie_story, movie_rating


    def KNN_Movie_Recommender(test_point, k):
        # Create dummy target variable for the KNN Classifier
        target = [0 for item in movie_titles]
        # Instantiate object for the Classifier
        model = KNearestNeighbours(data, target, test_point, k=k)
        # Run the algorithm
        model.fit()
        # Print list of 10 recommendations < Change value of k for a different number >
        table = []
        for i in model.indices:
            # Returns back movie title and imdb link
            table.append([movie_titles[i][0], movie_titles[i][2], data[i][-1]])
        print(table)
        return table


    def run():
        st.title("Entertain.me")  # Bigger title
        genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
                'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
        movies = [title[0] for title in movie_titles]
        recommended_movies = []  # List to store recommended movies
        
        cat_op = st.selectbox('Select Recommendation Type', category, key='rec_type_2')  # Unique key for the selectbox
        
        if cat_op == category[0]:
            st.warning('Please select Recommendation Type!!')
        elif cat_op == category[1]:
            select_movie = st.selectbox('Select movie: (Recommendation will be based on this selection)',
                                        [''] + movies, key='movie_select_2')  # Unique key for the selectbox
            if select_movie == '':
                pass
            else:
                no_of_reco = st.slider('Number of movies you want Recommended:', min_value=5, max_value=20, step=1, key='reco_number_2')
                genres = data[movies.index(select_movie)]
                test_points = genres
                table = KNN_Movie_Recommender(test_points, no_of_reco + 1)
                table.pop(0)
                c = 0
                st.success('Some of the movies from our Recommendation, have a look below')
                for movie, link, ratings in table:
                    if movie not in recommended_movies:
                        c += 1
                        recommended_movies.append(movie)
                        
                        with st.container():
                            st.write("---")
                            left_column, right_column = st.columns(2)
                            with left_column:
                                movie_poster_fetcher(link)
                            with right_column:
                                st.header(f"{c}. [{movie}]({link.split('?')[0]})")
                                st.markdown(f"IMDB Rating: {ratings} ⭐")
                                story, _ = get_movie_info(link)
                                st.write(story)

        elif cat_op == category[2]:
            sel_gen = st.multiselect('Select Genres:', genres, key='genre_select_2')  # Unique key for the multiselect
            if not sel_gen:
                # No genre selected, so don't output anything
                pass
            else:
                imdb_score = st.slider('Choose IMDb score:', 1, 10, 8, key='imdb_score_2')
                no_of_reco = st.number_input('Number of movies:', min_value=5, max_value=20, step=1, key='reco_number_genre_2')
                test_point = [1 if genre in sel_gen else 0 for genre in genres]
                test_point.append(imdb_score)
                table = KNN_Movie_Recommender(test_point, no_of_reco)
                c = 0
                st.success('What you might like')
                for movie, link, ratings in table:
                    if movie not in recommended_movies:
                        c += 1
                        recommended_movies.append(movie)
                        
                        with st.container():
                            st.write("---")
                            left_column, right_column = st.columns(2)
                            with left_column:
                                movie_poster_fetcher(link)
                            with right_column:
                                st.header(f"{c}. [{movie}]({link.split('?')[0]})")
                                st.markdown(f"IMDB Rating: {ratings} ⭐")
                                story, _ = get_movie_info(link)
                                st.write(story)

    run()

if __name__ == "__main__":
    app()  # Call the app function once
