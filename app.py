import streamlit as st
import pandas as pd

st.title('Sales/Purchase History')
st.text('This is a simple Streamlit app using Widgets') 
df=pd.DataFrame({'Purchase':[1200,1450,1100,12700,1340],'Sales':[12000,45000,1000,67000,3400]},index=['JAN','FEB','MAR','APR','MAY'] )
 
if st.checkbox(label='Show Frame'):
    st.write(df)


options =st.multiselect(label='Filter',options=df.columns)
 
st.line_chart(df[options])