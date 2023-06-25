import streamlit as st

st.write('Hello world!')
st.header('This is a header')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')