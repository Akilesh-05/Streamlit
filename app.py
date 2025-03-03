import streamlit as st
import pandas as pd
import numpy as np

from datetime import time

st.header("My Dashboard")
st.header("Data Visualization", anchor="viz")

# st.markdown("# heading")
# st.markdown("## subheading")
# st.markdown("[Google](https://www.google.com) for web search.")

# st.header("Streamlit")
# st.subheader("Streamlit subheading")

# st.write("Welcome!")

# if st.button("Click me!"):
#     st.write("Hello There!!")
# else:
#     st.write("Noo...")

st.slider("Enter a Number",0,50,25)
appointment = st.slider(
     "Schedule your appointment:",   # Label displayed above the slider
     value=(time(11, 30), time(12, 45))  # Default selected time range (11:30 AM - 12:45 PM)
)

st.write("Your selected appointment time:", appointment)

data=pd.DataFrame(np.random.randn(20,3), columns=["A","B","C"])
st.line_chart(data)

st.selectbox("Which is your Favorite color", ("Red","Blue","Green"))