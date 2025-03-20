import streamlit as st
import pickle

st.title("Khushi ho rahi hai dekh kar")


# st.markdown("""
# <style>
# body {
#   background: #ff0099; 
# }
# </style>
#     """, unsafe_allow_html=True)

file = open("performance.pkl", 'rb')
model = pickle.load(file)


# num = st.number_input(':red[Enter any number:]')

# text = st.text_input('Enter a text')

# x = st.chat_input()

# st.image()
uploaded_file = st.file_uploader("Choose a file")

num = st.number_input('Enter a number')
if st.button(f'Calculate the square of {num}'):
    st.text(num*num)

# x = st.slider('Select a value',0, 10, step=1)

# st.selectbox('Select any city',["Bhopal", "Mumbai", "Delhi"])

# color = st.color_picker("Pick A Color", "#00f900")
# st.write("The current color is", color)

