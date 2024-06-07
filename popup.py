import streamlit as st
from streamlit_modal import Modal
import json

# Simulate popup using a modal
modal = Modal("Information Input", key="popup")

# Initial page setup
def main():
    st.title("Main Page")
    st.write("Click the button below to enter information.")
    
    if st.button("Open Input Popup"):
        modal.open()

    if modal.is_open():
        with modal.container():
            st.write("This is the popup window")
            name = st.text_input("Enter your name:")
            age = st.number_input("Enter your age:", min_value=1, max_value=120)
            if st.button("Submit"):
                if 'details' not in st.session_state:
                    st.session_state['details'] = []
                st.session_state['details'].append({'name': name, 'age': age})
                st.experimental_rerun()

    if 'details' in st.session_state and st.session_state['details']:
        st.write(f"Latest Name: {st.session_state['details'][-1]['name']}")
        st.write(f"Latest Age: {st.session_state['details'][-1]['age']}")
        if st.button("Go to Information Page"):
            st.session_state['page'] = 'info'
            st.experimental_rerun()
        if st.button("Go to Full Details Page"):
            st.session_state['page'] = 'details'
            st.experimental_rerun()

def info_page():
    st.title("Information Page")
    if 'details' in st.session_state and st.session_state['details']:
        st.write(f"Latest Name: {st.session_state['details'][-1]['name']}")
        st.write(f"Latest Age: {st.session_state['details'][-1]['age']}")
    else:
        st.write("No information available. Please go back and enter your information.")
    
    if st.button("Go to Full Details Page"):
        st.session_state['page'] = 'details'
        st.experimental_rerun()
    if st.button("Go back to Main Page"):
        st.session_state['page'] = 'main'
        st.experimental_rerun()

def details_page():
    st.title("Full Details Page")
    if 'details' in st.session_state and st.session_state['details']:
        for i, detail in enumerate(st.session_state['details']):
            st.write(f"Entry {i + 1}:")
            st.write(f"Name: {detail['name']}")
            st.write(f"Age: {detail['age']}")
    else:
        st.write("No details available.")
    
    if st.button("Go back to Main Page"):
        st.session_state['page'] = 'main'
        st.experimental_rerun()

# Routing between pages
if 'page' not in st.session_state:
    st.session_state['page'] = 'main'

if st.session_state['page'] == 'main':
    main()
elif st.session_state['page'] == 'info':
    info_page()
elif st.session_state['page'] == 'details':
    details_page()
