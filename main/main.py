from dataclasses import dataclass

import requests
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass  # json serialize if not use, it errors
class Product(db.Model):
    id: int
    title: str
    image: str
    # declare type to see json api data
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)  # insert id as it is
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


# @app.route('api/products/<int:id>/like', methods=['POST'])
# def like(id):
#     # req = requests.get('http://docker.for.windows.localhost:8000/api/user')
#     # return jsonify(req.json())
#     pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
