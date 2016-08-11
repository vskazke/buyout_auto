from flask import render_template, jsonify, abort, redirect, url_for, request
import json
from app import app
from models import Models


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/models')
def models():
    brands = Models.select()
    brands = brands.order_by(Models.brand)

    return render_template('models.html', brands=brands)


@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    return name
