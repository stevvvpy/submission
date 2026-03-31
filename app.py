import streamlit as st
import pandas as pd
import joblib
from prediction import prediction
from data_prepocessing import data_preprocessing

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://png.pngtree.com/png-clipart/20190922/original/pngtree-educational-institute-icon-design-png-image_4775855.jpg", width=130)
with col2:
    st.header('Prediction student status (Prototype)')

data = pd.DataFrame(index=[0])

col1, col2, col3 = st.columns(3)

with col1:
    Debtor = st.selectbox(label="Debtor", options=["Yes", "No"], index=1)
    data["Debtor"] = 1 if Debtor == "Yes" else 0

with col2:
    Tuition_fees_up_to_date = st.selectbox(label="Tuition fees up to date", options=["Yes", "No"], index=0)
    data["Tuition_fees_up_to_date"] = 1 if Tuition_fees_up_to_date == "Yes" else 0

with col3:
    Scholarship_holder = st.selectbox(label="Scholarship holder", options=["Yes", "No"], index=0)
    data["Scholarship_holder"] = 1 if Scholarship_holder == "Yes" else 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    Unemployment_rate = float(st.number_input(label="Unemployment rate", min_value=0.0, max_value=100.0, value=11.56))
    data["Unemployment_rate"] = Unemployment_rate

with col2:
    Inflation_rate = float(st.number_input(label="Inflation rate", value=1.22))
    data["Inflation_rate"] = Inflation_rate

with col3:
    GDP = float(st.number_input(label="GDP", value=0.001))
    data["GDP"] = GDP

with col4:
    Admission_grade = float(st.number_input(label="Admission grade", min_value=0.0, max_value=200.0, value=0.0))
    data["Admission_grade"] = Admission_grade

col1, col2, col3 = st.columns(3)

with col1:
    Course = int(st.number_input(label="Course code", min_value=0, value=0))
    data["Course"] = Course

with col2:
    Previous_qualification = int(st.number_input(label="Previous qualification code", min_value=0, value=0))
    data["Previous_qualification"] = Previous_qualification

with col3:
    Previous_qualification_grade = float(st.number_input(label="Previous qualification grade", min_value=0.0, max_value=200.0, value=0.0))
    data["Previous_qualification_grade"] = Previous_qualification_grade

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label="Curricular units 1st sem enrolled", min_value=0, value=0))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

with col2:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label="Curricular units 1st sem evaluations", min_value=0, value=0))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

with col3:
    Curricular_units_1st_sem_approved = int(st.number_input(label="Curricular units 1st sem approved", min_value=0, value=0))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

with col4:
    Curricular_units_1st_sem_grade = float(st.number_input(label="Curricular units 1st sem grade", min_value=0.0, max_value=20.0, value=0.0))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label="Curricular units 2nd sem enrolled", min_value=0, value=0))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

with col2:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label="Curricular units 2nd sem evaluations", min_value=0, value=0))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

with col3:
    Curricular_units_2nd_sem_approved = int(st.number_input(label="Curricular units 2nd sem approved", min_value=0, value=0))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col4:
    Curricular_units_2nd_sem_grade = float(st.number_input(label="Curricular units 2nd sem grade", min_value=0.0, max_value=20.0, value=0.0))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.markdown("---")
    st.write("Prediction: {}".format(prediction(new_data)))