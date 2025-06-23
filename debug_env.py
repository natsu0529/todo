import streamlit as st
import sys
import os

st.set_page_config(page_title="Debug Environment")

st.title("🔍 Environment Debug Info")

st.header("Python Version")
st.code(sys.version)

st.header("Python Executable")
st.code(sys.executable)

st.header("Current Working Directory")
st.code(os.getcwd())

st.header("Files in Current Directory")
try:
    files = os.listdir('.')
    for file in sorted(files):
        st.write(f"- {file}")
except Exception as e:
    st.error(f"Error listing files: {e}")

st.header("Environment Variables (Selected)")
env_vars = ['PYTHONPATH', 'PATH', 'HOME', 'PWD']
for var in env_vars:
    value = os.environ.get(var, 'Not set')
    st.write(f"**{var}**: `{value}`")

st.header("Streamlit Version")
st.code(st.__version__)

st.success("If you can see this, Streamlit is working correctly!")
