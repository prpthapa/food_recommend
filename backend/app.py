import streamlit as st
import pickle
import pandas as pd

st.title('Food Recommender System')

food_dict = pickle.load(open('food_dict.pkl','rb'))
food = pd.DataFrame(food_dict)
similarity_matrix = pickle.load(open('similarity.pkl','rb'))
selected_food_item = st.selectbox('Select a food item',food['item'].values)

def recommend(selected_food_item):
    food_index = food[
        food["item"].str.lower() == selected_food_item.lower()
    ].index[0]

    scores = (similarity_matrix[food_index])
    food_list = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[1:6]

    recommend_food = []
    for i in food_list:
        recommend_food.append(food.iloc[i[0]]['item'])

    return recommend_food

if st.button('Recommend'):
    recommendations = recommend(selected_food_item)
    for item in recommendations:
        st.write(item)
