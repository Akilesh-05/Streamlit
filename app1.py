import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.header("Chart")

st.write("Hello!, *sungalesses*")

df=pd.DataFrame({
    "x" : [1,2,3,4,5,6],
    "y" : [1,4,9,16,25,36]
})

st.write(df)
st.write("The above table is **before**")

df1=pd.DataFrame(np.random.randn(200,3), columns=["A", "B", "C"])
c=alt.Chart(df1).mark_line().encode(
    x='A', y='B', tooltip=["A", "B", "C"]
)
st.write(c)