import os
import yaml
import json

from flask import render_template, jsonify, abort, redirect, url_for, request
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask_mail import Message
from app import app, mail
#  from config import ADMINS
from models import Models, Brands, Years, Pop_Brands

DIRNAME = './content/services'


@app.route('/')
def index():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    pop_brands = Pop_Brands.select()
    pop_brands = pop_brands.order_by(Pop_Brands.brand)
    print(url_for('static', filename='css/styles.css'))
    return render_template('index2.html',
                           brands=brands,
                           years=years,
                           pop_brands=pop_brands)


@app.route('/ocenka', methods=['GET', 'POST'])
def models():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    pop_brands = Pop_Brands.select()
    pop_brands = pop_brands.order_by(Pop_Brands.brand)

    return render_template('ocenka.html',
                           brands=brands,
                           years=years,
                           pop_brands=pop_brands)


@app.route('/service', methods=['GET', 'POST'])
def service():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    pop_brands = Pop_Brands.select()
    pop_brands = pop_brands.order_by(Pop_Brands.brand)

    return render_template('service.html',
                           brands=brands,
                           years=years,
                           pop_brands=pop_brands)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    pop_brands = Pop_Brands.select()
    pop_brands = pop_brands.order_by(Pop_Brands.brand)

    return render_template('about.html',
                           brands=brands,
                           years=years,
                           pop_brands=pop_brands)


@app.route('/about', methods=['GET', 'POST'])
def about():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    pop_brands = Pop_Brands.select()
    pop_brands = pop_brands.order_by(Pop_Brands.brand)

    return render_template('about.html',
                           brands=brands,
                           years=years,
                           pop_brands=pop_brands)


@app.route('/services/<service>', methods=['GET', 'POST'])
def different_services(service):
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    pop_brands = Pop_Brands.select()
    pop_brands = pop_brands.order_by(Pop_Brands.brand)
    filename = os.path.join(DIRNAME, service + '.yaml')
    if not os.path.exists(filename):
        abort(404)
    with open(filename) as f:
        services = yaml.load(f)
    return render_template('services.html',
                           services=services,
                           brands=brands,
                           years=years,
                           pop_brands=pop_brands)


@app.route('/<name>', methods=['GET', 'POST'])
def different_models(name):
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    try:
        model = Brands.select().where(Brands.brand == name).get()
        models = Models.select().where(Models.brand == model)
    except Brands.DoesNotExist:
        abort(404)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    pop_brands = Pop_Brands.select()
    pop_brands = pop_brands.order_by(Pop_Brands.brand)
    return render_template('brands.html', brands=brands, years=years,
                           pop_brands=pop_brands, model=model,
                           models=models)


@app.route('/getBrand', methods=['POST'])
def get_brand():
    name = request.form['name']
    return name


@app.route('/answer')
def answer():
    return render_template('answer.html')


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
    msg = Message("hello",
                  #  sender='agafonova.anastasia@gmail.com',
                  sender='anastacia111@yandex.ru',
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


@app.route('/short_result', methods=['POST'])
def short_result():
    brand = request.form['brand']
    model = request.form['model']
    year = request.form['year']
    name = request.form['name']
    phone = request.form['phone']
    msg = Message("hello",
                  #  sender='agafonova.anastasia@gmail.com',
                  sender='anastacia111@yandex.ru',
                  recipients=["vskazke.info@gmail.com"],)
    msg.body = 'text body'
    msg.html = "<ul>Автомобиль<li>Марка: %s</li>,\
            <li>модель: %s</li>,\
            <li>год: %s</li>,\
            <ul>Контактные данные<li>имя: %s</li>,\
            <li>тел: %s</li></ul>" %\
        (brand, model, year, name, phone)
    mail.send(msg)
    return 'Отправлено'


@app.route('/callBack', methods=['POST'])
def callBack():
    name = request.form['name']
    phone = request.form['phone']
    msg = Message("hello",
                  #  sender='agafonova.anastasia@gmail.com',
                  sender='anastacia111@yandex.ru',
                  recipients=["vskazke.info@gmail.com"],)
    msg.body = 'text body'
    msg.html = "<ul>Контактные данные<li>имя: %s</li>,\
            <li>тел: %s</li></ul>" %\
        (name, phone)
    mail.send(msg)
    return 'Отправлено'


@app.route('/message')
def test_message():
    msg = Message("hello",
                  #  sender='agafonova.anastasia@gmail.com',
                  sender='anastacia111@yandex.ru',
                  recipients=["vskazke.info@gmail.com"])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    #  with app.app_context():
    mail.send(msg)
    return 'Отправлено'
