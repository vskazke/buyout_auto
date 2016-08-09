from flask import render_template, jsonify, abort, redirect, url_for
import json
from app import app


@app.route('/page/1/')
@app.route('/')
def index():
    return render_template('index2.html')
