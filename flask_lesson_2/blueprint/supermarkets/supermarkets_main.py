import os
import uuid

from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from blueprint.supermarkets.forms import AddSupermarket
from utility import get_data, add_data, upload_image
from werkzeug.utils import secure_filename

supermarkets = Blueprint('supermarkets', __name__,
                         template_folder='template_s',
                         static_folder="static_s",
                         static_url_path='/blueprint/supermarkets/static_s', )

data = get_data("supermarkets.json")


@supermarkets.route('/supermarket/<s_id>')
def get_supermarket(s_id):
    for s in data:
        if s['id'] == s_id:
            return render_template('supermarket.html',
                                   name=s["name"],
                                   location=s["location"],
                                   img_name=s["img_name"],
                                   )
    return render_template('error_404.html')


@supermarkets.route('/supermarkets')
def get_all_supermarkets():
    url_arg = request.args.get('location', default='', type=str)
    if url_arg:
        filtered_data = []
        for each_super in data:
            if url_arg.lower() == each_super["location"]:
                filtered_data.append(each_super)
        return render_template('all_supermarkets.html', data=filtered_data)
    else:
        return render_template('all_supermarkets.html', data=data)


@supermarkets.route('/add_supermarket', methods=["GET", "POST"])
def add_supermarket():
    form = AddSupermarket()
    if form.validate_on_submit():
        img_file = request.files["image"]
        path = os.path.join("blueprint/supermarkets/static_s", secure_filename(img_file.filename))
        img_file.save(path)
        location = form.location.data
        new_supermarket = {
            "id": str(uuid.uuid4()),
            "name": form.name.data,
            "location": location.lower(),
            "img_name": img_file.filename
        }
        data.append(new_supermarket)
        add_data(data, "supermarkets.json")
        return redirect(url_for('supermarkets.get_all_supermarkets'))
    return render_template("add_supermarket.html", form=form)

