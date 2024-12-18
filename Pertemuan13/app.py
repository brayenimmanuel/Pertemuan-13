import streamlit as st

dashboard = st.Pages("./pages/dashboard.py", title="Dashboard") 
nabung = st.Pages("./pages/nabung.py", title="Nabung") 

pg = st.navigation({
    "Dashboard": [dashboard],
    "Nabung": [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state['Nabung'] = []

pg.run()