from tkinter import Y
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
#import dataset to use for exercise
my_dataset = pd.read_csv('Happiness.csv')
st.sidebar.header("Pick Two Variables for a Scatter plot")
x_val= st.sidebar.selectbox("Pick your X-axis Variable",my_dataset.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your Y-axis Variable",my_dataset.select_dtypes(include=np.number).columns.tolist())
st.header("This is a happiness score analysis")
st.write(my_dataset)
scatter = alt.Chart(my_dataset,title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip=[x_val,y_val,y_val])
st.altair_chart(scatter, use_container_width=True)
corr = round(my_dataset[x_val].corr(my_dataset[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")