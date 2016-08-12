from flask import render_template, jsonify, abort, redirect, url_for, request
import json
from app import app
from models import Models, Brands, Years


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/models', methods=['GET', ' POST'])
def models():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())

    return render_template('models.html', brands=brands, years=years)


@app.route('/getBrand', methods=['POST'])
def get_brand():
    name = request.form['name']
    return name


@app.route('/getModel', methods=['POST'])
def get_model():
    all_models = []
    name = request.form['name']
    brand = Brands.select().where(Brands.brand == name)
    models = Models.select().where(Models.brand == brand)
    for model in models:
        all_models.append(model.models)
    return jsonify(models=all_models)


@app.route('/changeModel', methods=['POST'])
def change_model():
    name = request.form['name']
    return name
