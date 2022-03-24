from flask import jsonify, request
from json import load
from dotenv import load_dotenv
from os import getenv

load_dotenv()

FILEPATH = getenv("FILEPATH")

def all_product():
    with open(FILEPATH) as fp:
        all_list_product = load(fp)

    return all_list_product


def get_product_by_id(product_id):

    all_list_product = all_product()

    filter_by = [product for product in all_list_product if product['id'] == product_id]

    if filter_by:
        return filter_by[0], 200

    return {'msg': 'not found product'}, 404

def get_all_product():
    all_list_product = all_product()

    return jsonify(all_list_product), 200
