from flask import render_template, jsonify, abort, redirect, url_for, request
import json
from app import app, mail
#  from config import ADMINS
from models import Models, Brands, Years
from flask_mail import Message

@app.route('/')
def index():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    return render_template('index2.html', brands=brands, years=years)


@app.route('/base')
def base():
    return render_template('base.html')


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


@app.route('/getYear', methods=['POST'])
def get_year():
    name = request.form['name']
    return name


@app.route('/getKpp', methods=['POST'])
def get_kpp():
    name = request.form['name']
    return name


@app.route('/result', methods=['POST'])
def result():
    brand = request.form['brand']
    model = request.form['model']
    year = request.form['year']
    kpp = request.form['kpp']
    km = request.form['km']
    price = request.form['price']
    name = request.form['name']
    phone = request.form['phone']
    print(brand)
    #  massage = 'ggggg'
    #  subject = "Марка: %s" % brand
    msg = Message("hello",
                  sender='agafonova.anastasia@gmail.com',
                  recipients=["vskazke.info@gmail.com"],)
    msg.body = 'text body'
    msg.html = "<ul>Автомобиль<li>Марка: %s</li>,\
            <li>модель: %s</li>,\
            <li>год: %s</li>,\
            <li>кпп: %s</li,\
            <li>пробег: %s</li>,\
            <li>цена: %s</li></ul>,\
            <ul>Контактные данные<li>имя: %s</li>,\
            <li>тел: %s</li></ul>" %\
        (brand, model, year, kpp, km, price, name, phone)
    mail.send(msg)
    return 'Отправлено'

    #  return jsonify(brand=brand,
                   #  model=model,
                   #  year=year,
                   #  kpp=kpp,
                   #  km=km,
                   #  price=price,
                   #  name=name,
                   #  phone=phone,
                   #  comment=comment)


@app.route('/message')
def test_message():
    msg = Message("hello",
                  sender='agafonova.anastasia@gmail.com',
                  recipients=["vskazke.info@gmail.com"])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    #  with app.app_context():
    mail.send(msg)
    return 'Отправлено'
