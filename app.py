import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url= "https://api.themoviedb.org/3/movie/{}?api_key=ce44709c04b8bce655c59880ff8b4f75&language=en-US".format(movie_id)    
    # url= 'https://api.themoviedb.org/3/movie/{285}?api_key=ce44709c04b8bce655c59880ff8b4f75&language=en-US'.format(movie_id)
    data = requests.get(url)
    data= data.json()
    poster_path =data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path

    return full_path    

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x:x[1])
    recommendation_movie = []
    recommendation_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommendation_poster.append(fetch_poster(movie_id))
        recommendation_movie.append(movies.iloc[i[0]].title)
    return recommendation_movie,recommendation_poster

st.header("Movies Recommendation System")
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity_list.pkl', 'rb'))

movies_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommender', movies_list
)
if st.button('Show recommendation'):

    recommendation_movie, recommendation_poster = recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendation_movie[0])
        st.image(recommendation_poster[0])

    with col2:
        st.text(recommendation_movie[1])
        st.image(recommendation_poster[1])

    with col3:
        st.text(recommendation_movie[2])
        st.image(recommendation_poster[2])
    
    with col4:
        st.text(recommendation_movie[3])
        st.image(recommendation_poster[3])

    with col5:
        st.text(recommendation_movie[4])
        st.image(recommendation_poster[4])

st.text("Enjoy watching!")