import os
import uuid

from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from utility import get_data, add_data, upload_image_product
from blueprint.products.forms import AddProduct
from werkzeug.utils import secure_filename


products = Blueprint('products', __name__,
                     template_folder='template_p',
                     static_folder='static_p',
                     static_url_path='/blueprint/products/static_p', )


data = get_data("products.json")


@products.route('/product/<id>', methods=["GET"])
def get_product(id):
    for product in data:
        if product['id'] == id:
            return render_template('product.html',
                                   name=product["name"],
                                   description=product["description"],
                                   img_name=product["img_name"],
                                   price=product["price"]
                                   )
    return render_template('error_404.html')


@products.route('/all-products')
def get_all_products():
    url_arg = request.args.get('price', default='')
    if url_arg:
        filtered_data = []
        for item in data:
            if float(url_arg) == item['price']:
                filtered_data.append(item)
        return render_template('all_products.html', data=filtered_data)
    else:
        return render_template('all_products.html', data=data)


@products.route('/add-product', methods=["GET", "POST"])
def add_product():
    form = AddProduct()
    if form.validate_on_submit():
        new_product = {
            "id": str(uuid.uuid4()),
            "name": form.name.data,
            "description": form.description.data,
            "img_name": upload_image_product(),
            "price": form.price.data
        }
        data.append(new_product)
        add_data(data, "products.json")
        flash('Product added!', 'success')
        return redirect(url_for('products.get_all_products'))
    return render_template('add_product.html', form=form)

