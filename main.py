import streamlit as st
import torch
import torch.nn as nn

torch.manual_seed(31337)

st.title("Lorem Ipsum")
st.text("Lorem ipsum dolor sit amet")

st.header("Dummy model")
num = st.number_input("Input a number and it will be doubled")
butt = st.button("Test button")

model = nn.Linear(1, 1)

#return value in textbox when button pressed
if butt:
    val = model(torch.tensor([num]))
    st.text("Result: " + str(val.item()))



