# app.py
import streamlit as st
import pandas as pd
df = pd.DataFrame({'first column':[1,2,3],
                   'second column':[10,20,30]})
st.title('Hello Oksusu^^')
st.write(df)
st.bar_chart(df)
df
df
st.write('# oksusu^^')
st.write('## oksusu^^')