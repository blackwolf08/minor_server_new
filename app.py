from flask import Flask, request, send_file
import base64
import numpy as np
import tensorflow
import keras
from keras.preprocessing import image
from keras.models import load_model
from flask_ngrok import run_with_ngrok
from PIL import ImageTk, Image
import fpdf
from datetime import date
import tensorflow as tf
app = Flask(__name__) 


@app.route('/', methods = ['GET'])
def get_root():
    return "Hello World"

if __name__ == '__main__':
    app.config["JSON_SORT_KEYS"] = False
    app.run(host='127.0.0.1', port=8080, debug=True)
