pip install jsonlines

import json
import glob
from pprint import pprint
import streamlit as st
import pandas as pd

st.header("Political Party Classification")
st.write("""Hello! This is Simon, Johannes and Dominik. Our aim is to predict the affiliation to a political party from Tweets. """)


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

number = st.slider("Pick a Number!", 1, 30)


