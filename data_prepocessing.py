import joblib
import numpy as np
import pandas as pd

# Buat scaler dan model
pca = joblib.load("model/pca.joblib")
scaler_admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Course = joblib.load("model/scaler_Course.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Debtor = joblib.load("model/scaler_Debtor.joblib")
scaler_GDP = joblib.load("model/scaler_GDP.joblib")
scaler_Inflation_rate = joblib.load("model/scaler_Inflation_rate.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Previous_qualification = joblib.load("model/scaler_Previous_qualification.joblib")
scaler_scholarship_holder = joblib.load("model/scaler_Scholarship_holder.joblib")
scaler_Tuition_fees_up_to_date = joblib.load("model/scaler_Tuition_fees_up_to_date.joblib")
scaler_Unemployment_rate = joblib.load("model/scaler_Unemployment_rate.joblib")

pca_cols = ['Debtor', 'Tuition_fees_up_to_date', 
    'Scholarship_holder', 'Unemployment_rate',
    'Inflation_rate', 'GDP','Admission_grade', 'Course',
    'Previous_qualification', 'Previous_qualification_grade',
    'Curricular_units_1st_sem_enrolled', 
    'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved', 
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations', 
    'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade']

def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    df['Debtor'] = scaler_Debtor.transform(np.asarray(data['Debtor']).reshape(-1,1))[0]
    df['Tuition_fees_up_to_date'] = scaler_Tuition_fees_up_to_date.transform(np.asarray(data['Tuition_fees_up_to_date']).reshape(-1,1))[0]
    df['Scholarship_holder'] = scaler_scholarship_holder.transform(np.asarray(data['Scholarship_holder']).reshape(-1,1))[0]
    df['Unemployment_rate'] = scaler_Unemployment_rate.transform(np.asarray(data['Unemployment_rate']).reshape(-1,1))[0]
    df['Inflation_rate'] = scaler_Inflation_rate.transform(np.asarray(data['Inflation_rate']).reshape(-1,1))[0]
    df['GDP'] = scaler_GDP.transform(np.asarray(data['GDP']).reshape(-1,1))[0]
    df['Admission_grade'] = scaler_admission_grade.transform(np.asarray(data['Admission_grade']).reshape(-1,1))[0]
    df['Course'] = scaler_Course.transform(np.asarray(data['Course']).reshape(-1,1))[0]
    df['Previous_qualification'] = scaler_Previous_qualification.transform(np.asarray(data['Previous_qualification']).reshape(-1,1))[0]
    df['Previous_qualification_grade'] = scaler_Previous_qualification_grade.transform(np.asarray(data['Previous_qualification_grade']).reshape(-1,1))[0]
    df['Curricular_units_1st_sem_enrolled'] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data['Curricular_units_1st_sem_enrolled']).reshape(-1,1))[0]
    df['Curricular_units_1st_sem_evaluations'] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_evaluations']).reshape(-1,1))[0]
    df['Curricular_units_1st_sem_approved'] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data['Curricular_units_1st_sem_approved']).reshape(-1,1))[0]    
    df['Curricular_units_1st_sem_grade'] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data['Curricular_units_1st_sem_grade']).reshape(-1,1))[0]
    df['Curricular_units_2nd_sem_enrolled'] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data['Curricular_units_2nd_sem_enrolled']).reshape(-1,1))[0]
    df['Curricular_units_2nd_sem_evaluations'] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data['Curricular_units_2nd_sem_evaluations']).reshape(-1,1))[0]
    df['Curricular_units_2nd_sem_approved'] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data['Curricular_units_2nd_sem_approved']).reshape(-1,1))[0]
    df['Curricular_units_2nd_sem_grade'] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data['Curricular_units_2nd_sem_grade']).reshape(-1,1))[0]

    df[["pc_1", "pc_2", "pc_3","pc_4", "pc_5", "pc_6", "pc_7", "pc_8", "pc_9", "pc_10"]] = pca.transform(data[pca_cols])
    df.drop(columns=pca_cols, axis=1, inplace=True)

    return df
