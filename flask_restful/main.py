from datetime import timedelta

from flask import Flask

from config import run_config
from blueprint.rooms.main_rooms import rooms
from blueprint.tenants.main_tenants import tenants
from blueprint.staff.main_staff import staff
from blueprint.rooms_tenants import rooms_tenants
from blueprint.rooms_staff import rooms_staff
from create_db import create_db
from db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)

    app.register_blueprint(create_db)
    app.register_blueprint(rooms)
    app.register_blueprint(staff)
    app.register_blueprint(tenants)
    app.register_blueprint(rooms_tenants)
    app.register_blueprint(rooms_staff)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)

