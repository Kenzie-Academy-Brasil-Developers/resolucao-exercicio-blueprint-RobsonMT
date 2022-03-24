from flask import Flask
from .product_route import bp_products

def init_app(app: Flask):
    app.register_blueprint(bp_products)