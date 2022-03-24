from cProfile import run
from flask import Blueprint
from app.controllers import product_controller

bp_products = Blueprint("products", __name__)

bp_products.get('/products')(product_controller.get_all_product)
bp_products.get('/products/<int:product_id>')(product_controller.get_product_by_id)