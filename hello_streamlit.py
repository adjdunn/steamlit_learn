# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:39:08 2023

@author: -
"""

import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header('st.write')

st.write("Hello, *World!* :sunglasses:")


st.write(1234)


df = pd.DataFrame({'first_column': [1, 2, 3, 4], 
                   'second_column': ['cat', 'man', 'apple', 'paul']})

st.write(df)


st.write('Below is a dataframe:', df, 'Above is a dataframe.')


df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)