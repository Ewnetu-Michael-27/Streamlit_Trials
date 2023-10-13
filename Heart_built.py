from inspect import stack
from tkinter import Grid
import streamlit as st
import seaborn as sns
import altair as alt
from altair import datum
import matplotlib.pyplot as plt
import hiplot as hip 
import pandas as pd
import plotly.express as px



col=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]
df_heart=pd.read_csv("df_heart_clean.csv")


st.set_page_config(
    page_title="Intro CAD and The Heart Dataset",
)

st.title("Main Page")
st.write("*Regarding prediction model, check second page on sidebar* :sunglasses:")
st.sidebar.success("Select a page above.")


option=st.selectbox(
    "The variables are medical terminologies. Choose from below to see further discription about them",
    ("age","sex", "cp", "trestbps", "chol", 
     "fbS", "restecg", "thalach", 
     "exang", "oldpeak", "slope", "ca", "thal", "num")
)

if option=="age":
    st.write("Age of the Individual")
elif option=="sex":
    st.write("Sex of the Individual")
elif option=="cp":
    st.write("Chest Pain Types")
elif option=="trestbps":
    st.write("Resting Blood Pressure in mm of Hg at the admission to Hospital")
elif option=="chol":
    st.write("Serum Cholestrol in mg/dl")
elif option=="fbs":
    st.write("Fasting Blood Sugar")
elif option=="restecg":
    st.write("Resting Electrocardiographic Results")
elif option=="thalach":
    st.write("maximum Heart Rate Achieved")
elif option=="exang":
    st.write("Exercise Induced Angina")
elif option=="oldpeak":
    st.write("ST Depression Induced by excercise relative to rest")
elif option=="slope":
    st.write("The Slope of the peak exercise ST segment")
elif option=="ca":
    st.write("Number of major vessels colored by fluroscopy")
elif option=="thal":
    st.write("Thallium scintigraphy")
elif option=="num":
    st.write("Diagnosis of Heart Disease (Angiographic Disease Status)")

st.text("")
st.markdown("***")

option2=st.selectbox(
    "Pick a variable to see its relatioship with num",
    ("age","sex", "cp", "trestbps", "chol", 
     "fbs", "restecg", "thalach", 
     "exang", "oldpeak", "slope", "ca", "thal", "num")
)


#Continous variable
if option2 in ["oldpeak", "trestbps", "thalach", "age", "chol"]:
    chart_alt=alt.Chart(df_heart).mark_bar().encode(
    alt.X(option2, type='quantitative'),
    alt.Y('count()', type='quantitative'),
    color='num:N').interactive()

    st.altair_chart(chart_alt)

#categorical variables
elif option2 in ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal", "num"]:
    pd_plot=pd.crosstab(df_heart[option2],df_heart["num"]).plot(kind='bar')
    st.pyplot(pd_plot.figure)

st.text("")
st.markdown("***")

st.write("Click on the button below to see Parrllel plot of Age, Thalach, Oldpeak, num")

x=st.button("Parallel Plot")

if x:
    fig = px.parallel_coordinates(df_heart[["age","thalach","oldpeak","num"]], color="num", labels={"num": "Num",
                "age": "Age", "thalach": "Thalach",
                "oldpeak": "Oldpeak",},
                             color_continuous_scale=px.colors.diverging.Tealrose,
                             color_continuous_midpoint=2)
    st.plotly_chart(fig)

