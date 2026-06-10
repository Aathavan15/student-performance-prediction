import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
from datetime import datetime

# Load Model

model = joblib.load("student_marks_model.pkl")

st.set_page_config(
page_title="Student Performance Predictor",
page_icon="📚",
layout="centered"
)

st.title("📚 Student Performance Predictor")

# Inputs

age = st.number_input(
"Age",
min_value=15,
max_value=30,
value=20
)

gender_text = st.selectbox(
"Gender",
["Male", "Female"]
)

gender = 1 if gender_text == "Male" else 0

study_hours_per_day = st.slider(
"Study Hours Per Day",
0.0,
12.0,
5.0
)

social_media_hours = st.slider(
"Social Media Hours",
0.0,
12.0,
2.0
)

netflix_hours = st.slider(
"Netflix Hours",
0.0,
12.0,
1.0
)

part_time_job_text = st.selectbox(
"Part Time Job",
["No", "Yes"]
)

part_time_job = 1 if part_time_job_text == "Yes" else 0

attendance_percentage = st.slider(
"Attendance Percentage",
0.0,
100.0,
85.0
)

sleep_hours = st.slider(
"Sleep Hours",
0.0,
12.0,
7.0
)

diet_quality_text = st.selectbox(
"Diet Quality",
["Poor", "Average", "Good"]
)

diet_map = {
"Poor": 0,
"Average": 1,
"Good": 2
}

diet_quality = diet_map[diet_quality_text]

exercise_frequency = st.slider(
"Exercise Frequency (Days/Week)",
0,
7,
3
)

parental_education_level_text = st.selectbox(
"Parental Education",
["High School", "Bachelor", "Master"]
)

parent_map = {
"High School": 0,
"Bachelor": 1,
"Master": 2
}

parental_education_level = parent_map[parental_education_level_text]

internet_quality_text = st.selectbox(
"Internet Quality",
["Poor", "Average", "Good"]
)

internet_map = {
"Poor": 0,
"Average": 1,
"Good": 2
}

internet_quality = internet_map[internet_quality_text]

mental_health_rating = st.slider(
"Mental Health Rating",
1,
10,
7
)

extracurricular_participation_text = st.selectbox(
"Extracurricular Participation",
["No", "Yes"]
)

extracurricular_participation = 1 if extracurricular_participation_text == "Yes" else 0  

# Predict

if st.button("Predict Score"):

    data = np.array([[
    
    age,
    gender,
    study_hours_per_day,
    social_media_hours,
    netflix_hours,
    part_time_job,
    attendance_percentage,
    sleep_hours,
    diet_quality,
    exercise_frequency,
    parental_education_level,
    internet_quality,
    mental_health_rating,
    extracurricular_participation,
    
    ]])

    prediction = model.predict(data)[0]

    prediction = np.clip(prediction,0,100)

   
# Save for Power BI
    new_record = pd.DataFrame({
    "Timestamp": [datetime.now()],
    "Age": [age],
    "Gender": [gender_text],
    "Study_Hours_Per_Day": [study_hours_per_day],
    "Social_Media_Hours": [social_media_hours],
    "Netflix_Hours": [netflix_hours],
    "Part_Time_Job": [part_time_job_text],
    "Attendance_Percentage": [attendance_percentage],
    "Sleep_Hours": [sleep_hours],
    "Diet_Quality": [diet_quality_text],
    "Exercise_Frequency": [exercise_frequency],
    "Parental_Education_Level": [parental_education_level_text],
    "Internet_Quality": [internet_quality_text],
    "Mental_Health_Rating": [mental_health_rating],
    "Extracurricular_Participation": [extracurricular_participation_text],
    "Predicted_Score": [prediction]
    })

    st.success(f"Predicted_Score: {prediction:.2f}")

    file_name = "predictions.csv"

    if os.path.exists(file_name):
        new_record.to_csv(
        file_name,
        mode="a",
        header=False,
        index=False
        )
    else:
        new_record.to_csv(
        file_name,
        index=False
        )















    #data = np.array([[
    #   age,     # age
    #    1,       # gender
    #    study_hours,
    #    social_media,
    #    1,       # netflix_hours
    #    0,       # part_time_job
    #    attendance,
    #    sleep_hours,
    #    2,       # diet_quality
    #    3,       # exercise_frequency
    #    1,       # parental_education_level
    #    2,       # internet_quality
    #    mental_health,
    #    1        # extracurricular_participation
    #]])

    #prediction = model.predict(data)[0]

    #prediction = np.clip(prediction,0,100)


    #st.success(
    #    f"Predicted Exam Score: {prediction:.2f}"
    #)