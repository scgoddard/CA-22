import streamlit as st
import pandas as pd
import numpy as np

# App Setup
st.title("Simple Streamlit App")

# Data Display
st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# User Interaction
if st.button('Say hello'):
    st.write('Why hello there!')
else:
    st.write('Goodbye')

# Data Visualization
data = np.random.randn(20, 3)
df2 = pd.DataFrame(data, columns=['a', 'b', 'c'])
st.line_chart(df2)
