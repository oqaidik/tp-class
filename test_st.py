import streamlit as st
with st.sidebar:
    x = st.radio('Pick your gender',['Male','Female'])

if x=="Male":
    st.write("Hello ,let's learn how to build a streamlit app together")
    st.image("icone1.jpg")
    st.checkbox('yes')
    st.button('Click')
if x=="Female":
    st.selectbox('Pick your gender',['Male','Female'])
    st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
    st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    st.slider('Pick a number', 0,50)
    st.number_input('Pick a number', 0,10)
    st.text_input('Email address')
    st.date_input('Travelling date')
    st.time_input('School time')
    st.text_area('Description')
    st.file_uploader('Upload a photo')
    st.color_picker('Choose your favorite color')


