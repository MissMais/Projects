import streamlit as st
import pickle


st.title("Welcome to Student Performance Check Application")

file = open("performance.pkl", 'rb')
model = pickle.load(file)

hours_studied = st.selectbox('Enter the number of hours you studied:', [0, 1, 2, 3, 4, 5, 6, 7, 8])
previous_score = st.number_input('Enter your previous score:')
hours_sleep = st.selectbox('Enter the number of hours you sleep:', [3, 4, 5, 6, 7])
sample_paper = st.selectbox('Number of sample papers you solved:', [0, 1, 2, 3, 4, 5])
activity = st.radio('Are you involved in extra curricular activities?', ["Yes", "No"])

yes = 0
no = 0
if activity == 'Yes':
    yes += 1
else:
    no += 1

if st.button("Predict the Performance"):
    res = model.predict([[hours_studied, previous_score, hours_sleep, sample_paper, no, yes]])
    st.text(f":red[Your Performance Index is: {int(res)}]")
