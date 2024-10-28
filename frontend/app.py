
import streamlit as st
import requests
import pandas as pd
import numpy as np


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
st.header('The list of files in the folder')

# list of files
response = requests.get(f"{base_url}/file_list").json()
st.dataframe(pd.DataFrame.from_dict(response.values()))

# Insert a chat message container.
with st.chat_message("user"):
   st.write("Hello 👋")
   st.line_chart(np.random.randn(30, 3))

# Display a chat input widget.
st.chat_input("Say something")

st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

st.button('Hit me')
# st.data_editor('Edit data', data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
# st.download_button('On the dl', data)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')
