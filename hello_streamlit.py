# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:39:08 2023

@author: -
"""

import streamlit as st
from datetime import time, datetime


st.header('st.slider')


st.subheader('Slider')

age = st.slider("How old are you?", 0, 130, 25)
st.write("I am ", age, " years old.")


st.subheader('Range Slider')

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

st.write("Values: ", values)

st.subheader('Range Time Slider:')

appointment = st.slider('Schedule your appointment:', value=(time(11, 30), time(12, 45)))

st.write("You're scheduled for: ", appointment)

st.subheader('Datetime Slider')

start_time = st.slider("When do you want to start: ",
                       value=datetime(2023, 3, 12, 14, 30),
                       format="MM/DD/YY - hh:mm")

st.write("Start Time: ", start_time)
                        
                        