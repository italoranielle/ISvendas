from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/isvenda'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    suplayer = db.Column(db.String(20), nullable=False)
    wifi = db.Column(db.Boolean, nullable=True)
    zegbee = db.Column(db.Boolean, nullable=True)
    rf =  db.Column(db.Boolean, nullable=True)
    attrs = db.Column(db.Text, nullable=True)
    barcode = db.Column(db.String(20), nullable=False)
    price_sell = db.Column(db.Float,nullable=False)  

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    cliente = db.Column(db.Stringg(250),nullable = False)
    total_price = db.Column(db.Float,nullable=False)

class ItenSale(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    id_iten = db.C