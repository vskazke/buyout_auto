from flask import render_template, jsonify, abort, redirect, url_for, request
from werkzeug.utils import secure_filename
from flask import send_from_directory
import json
import os
from app import app, mail
#  from config import ADMINS
#  from models import Models, Brands, Years, Pop_Brands
from flask_mail import Message

@app.route('/')
def index():
    return 'hello world'
