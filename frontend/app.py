
import streamlit as st
import requests
import pandas as pd


st.set_page_config(layout="wide")


### API call ==================================================================
base_url = "http://127.0.0.1:8000"
# base_url = "https://power-v2-pdymu2v2na-ew.a.run.app"
#------------------------------------------------------------------------------



# ==============================================================================
# ====================== Streamlit Interface ===================================

### Sidebar ====================================================================
st.sidebar.markdown(f"""
   # User Input
   """)



### Main window ====================================================================

f"""
# Experimental Data Digitalization
"""

### Get metadata
st.title('The list of files in the folder')

# list of files
response = requests.get(f"{base_url}/file_list").json()
st.dataframe(pd.DataFrame.from_dict(response.values()))
