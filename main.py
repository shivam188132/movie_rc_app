import pickle
import streamlit as st
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
# print(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
# print(titles)

selected_movie_name = st.selectbox(
    "How would you like to be connected? ", movies['title'].values)

def movie_poster(id):
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{id}?api_key=8a5a4bb0bf23e25aaeb0c8b917338db6").json()
    full_url ="https://image.tmdb.org/t/p/w500/"+ str(response['poster_path'])
    return full_url



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    # print(movies[movies['title'] == movie])
    distances = similarity[index]
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        # fetch poster from api

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(movie_poster(movie_id))
    return recommended_movies, recommended_movie_posters


if st.button('Recommended'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
