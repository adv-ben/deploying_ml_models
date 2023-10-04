import streamlit as st
import torch

st.title("Hallo!!")
st.text("Lorem ipsum")

button_pressed = st.button("Click me")

if  button_pressed:
    st.text("You clicked the button!")