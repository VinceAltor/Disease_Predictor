
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

# loading the saved models
st.set_page_config(page_title="Disease Predictor", page_icon=":tada:", layout="wide")

diabetes_model = pickle.load(open('C:/Users/User/Desktop/DISEASE PREDICTION SYSTEM/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/User/Desktop/DISEASE PREDICTION SYSTEM/heart_disease_model.sav','rb'))

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_dd7yh7kk.json")
lottie_coding2 = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_g0xeklmz.json")
lottie_codinga = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_ginda0jy.json")
lottie_coding3 = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_g0xeklmz.json")


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Home','Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)


if (selected == 'Home'):

    left_column, right_column = st.columns(2)


    with right_column:
        st_lottie(lottie_coding, height=200, key="coding")

    new_title = '<p style="font-family:sans-serif; color:blue; font-size: 70px;"> DISEASE PREDICTOR</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:black; font-size: 25px;"> Welcome to Disease predictor!!</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:black; font-size: 25px;"> Our Machine learning based model can predict whether you are any health ailments like Diabetes and Heart Diseases or not </p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:black; font-size: 25px;"> Please Check out Diabetes predictor and heart ailemnt predictor by clicking on Slidebars.</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:black; font-size: 25px;"> THANK YOU and have a nice day!! </p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:black; font-size: 20px;"> Developed by: Vinay and Team</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    with left_column:
        st_lottie(lottie_codinga, height=200, key="co")
    
    






# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'You are diagnosed with diabetes, Please consult nearby doctor'
        else:
          diab_diagnosis = 'You are not diagnosed with diabetes'

    st_lottie(lottie_coding2, height=200, key="cod")    
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')
    

    
    
    age = st.text_input('Age')
        
    sex = st.text_input('Sex')
        
    cp = st.text_input('Chest Pain types')
        
    trestbps = st.text_input('Resting Blood Pressure')
        
    chol = st.text_input('Serum Cholestoral in mg/dl')
        
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    restecg = st.text_input('Resting Electrocardiographic results')
        
    thalach = st.text_input('Maximum Heart Rate achieved')
        
    exang = st.text_input('Exercise Induced Angina')
        
    oldpeak = st.text_input('ST depression induced by exercise')
        
    slope = st.text_input('Slope of the peak exercise ST segment')
        
    ca = st.text_input('Major vessels colored by flourosopy')
        
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
    st_lottie(lottie_coding3, height=200, key="coder")    
    st.success(heart_diagnosis)
