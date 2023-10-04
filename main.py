"""
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
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)


