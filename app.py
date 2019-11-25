from flask import Flask, request, send_file
import base64
import numpy as np
import tensorflow
import keras
from keras.preprocessing import image
from keras.models import load_model
from PIL import ImageTk, Image
import fpdf
from datetime import date
import tensorflow as tf
app = Flask(__name__) 


@app.route('/', methods = ['GET'])
def hello():
    return "Hello World"
