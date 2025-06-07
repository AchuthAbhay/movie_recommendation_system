import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os  

def fetch_poster(movie_id):
    api_key = "df3fbef252815eeb3e593d6f3c46e004"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies =[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


similarity= pickle.load(open('similarity.pkl','rb'))       
movies_dict=pickle.load(open('movie_dict.pkl','rb'))


movies=pd.DataFrame(movies_dict)


st.title('MOVIE RECOMMENDER SYSTEM')
selected = st.selectbox(
    "Select a movie",
    movies['title'].values,
)
st.write("You selected:", selected)



if st.button('Recommend'):
  names,posters=recommend(selected)
  col1,col2,col3,col4,col5=st.columns(5)
  with col1:
      st.text(names[0])
      st.image(posters[0])
  with col2:
      st.text(names[1])
      st.image(posters[1])
  with col3:
      st.text(names[2])
      st.image(posters[2]) 
  with col4:
      st.text(names[3])
      st.image(posters[3])
  with col5:
      st.text(names[4])
      st.image(posters[4])               

# Auto-download similarity.pkl if missing
file_path = 'similarity.pkl'
if not os.path.exists(file_path):
    st.write("Downloading similarity matrix from Google Drive...")
    url = 'https://drive.google.com/file/d/1_zehUgoZj1ijUUWY4yj_dC9A8WzehhY4/view?usp=drive_link'  # Replace YOUR_FILE_ID
    gdown.download(url, file_path, quiet=False)