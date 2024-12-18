import streamlit as st

st.title("Ini Halaman Dashboard")

st.session_state["Nabung"]
jumlah = 0

for session in st.session_state["Nabung"]:
    jumlah += session["Npminal"]

st.write("Total nominal yang ditabung", jumlah)