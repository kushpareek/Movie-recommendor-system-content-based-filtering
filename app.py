import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:50]
    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies_list = pd.DataFrame(movies_dict)
st.title('Movie Recommeder System')
#streamlit library is used as alternative of Flask
selected_movie_name = st.selectbox(
    'Search Movies',
    (movies_list['title'].values))
if st.button('Recommend'):
    recomendations = recommend(selected_movie_name)
    for i in recomendations:
        st.write(i)