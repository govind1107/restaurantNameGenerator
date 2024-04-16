import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import langchain_code

st.title("Restaurant Name Generator")


cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Arabic","Italian","Mexican","Chinese","Japanese","African","American"))




if cuisine:
    response = langchain_code.generate_restaurant(cuisine)
    st.header(response['restaurant_name'].strip())
    menu = response['menu'].strip().split(',')

    print(response['menu'])
    
    st.write("Menu Items")

    for item in menu:
        st.write('-',item)

