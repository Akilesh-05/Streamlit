import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

df_agg=pd.read_csv("D:/Streamlit/Aggregated_Metrics_By_Video.csv").iloc[1:,:]

df_agg_sub=pd.read_csv("D:/Streamlit/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv")
df_comments=pd.read_csv("D:/Streamlit/Aggregated_Metrics_By_Video.csv")
df_time=pd.read_csv("D:/Streamlit/Video_Performance_Over_Time.csv")
