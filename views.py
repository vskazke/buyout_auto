from flask import render_template, jsonify, abort, redirect, url_for, request
from werkzeug.utils import secure_filename
from flask import send_from_directory
import json
import os
from app import app, mail
#  from config import ADMINS
from models import Models, Brands, Years, Pop_Brands
from flask_mail import Message

@app.route('/')
def index():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    pop_brands = Pop_Brands.select()
    pop_brands = pop_brands.order_by(Pop_Brands.brand)
    return render_template('index2.html', brands=brands, years=years, pop_brands=pop_brands)


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/ocenka', methods=['GET', 'POST'])
def models():
    brands = Brands.select()
    brands = brands.order_by(Brands.brand)
    years = Years.select()
    years = years.order_by(Years.year.desc())
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join('/home/agafia/0/byuout_auto', filename))
        #  with app.open_resource(filename) as fp:
                #  msg.attach(filename, "image/png", fp.read())
                #  msg.html = "<img src= %s>" % (fp)

    return render_template('ocenka.html', brands=brands, years=years)


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
    #  photo = request.form['photo']
    #  print(photo)
    #  file = request.files['file']
    #  print(file)
    #  file.save(os.path.join('/home/agafia/0/byuout_auto', filename))
    msg = Message("hello",
                  sender='agafonova.anastasia@gmail.com',
                  recipients=["vskazke.info@gmail.com"],)
    #  with app.open_resource(filename) as fp:
            #  msg.attach(filename, "image/png", fp.read())
    #  msg.body = 'text body'
    #  massage = 'ggggg'
    #  subject = "Марка: %s" % brand
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
    #  os.remove(os.path.join('/home/agafia/0/byuout_auto', filename))
    return 'Отправлено'

@app.route('/short_result', methods=['POST'])
def short_result():
    brand = request.form['brand']
    model = request.form['model']
    year = request.form['year']
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
            <ul>Контактные данные<li>имя: %s</li>,\
            <li>тел: %s</li></ul>" %\
        (brand, model, year, name, phone)
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


@app.route('/callBack', methods=['POST'])
def callBack():
    name = request.form['name']
    phone = request.form['phone']
    msg = Message("hello",
                  sender='agafonova.anastasia@gmail.com',
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
                  sender='agafonova.anastasia@gmail.com',
                  recipients=["vskazke.info@gmail.com"])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    #  with app.app_context():
    mail.send(msg)
    return 'Отправлено'

@app.route('/photo', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            file2 = request.files['file2']
            print(file)
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            filename = secure_filename(file.filename)
            filename2 = secure_filename(file2.filename)
            file.save(os.path.join('/home/agafia/0/byuout_auto', filename))
            file2.save(os.path.join('/home/agafia/0/byuout_auto', filename2))
            msg = Message("hello",
                          sender='agafonova.anastasia@gmail.com',
                          recipients=["vskazke.info@gmail.com"],)
            #  msg.body = 'text body'
            #  with app.open_resource(filename) as fp:
                    #  msg.attach(filename, "image/png", fp.read())
                    #  #  msg.html = "<img src= %s>" % (fp)
            #  with app.open_resource(filename2) as fp:
                    #  msg.attach(filename2, "image/png", fp.read())
            #  mail.send(msg)
            #  os.remove(os.path.join('/home/agafia/0/byuout_auto', filename))
            #  return redirect(url_for('uploaded_file',
                                        #  filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <p><input type=file name=file2>
    <input  value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('/home/agafia/',
                                          filename)
