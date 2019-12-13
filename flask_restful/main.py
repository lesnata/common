from flask import Flask
from config import run_config
from blueprint.rooms.main_rooms import rooms
from blueprint.tenants.main_tenants import tenants
from blueprint.staff.main_staff import staff


app = Flask(__name__)
app.config.from_object(run_config())
app.register_blueprint(rooms)
app.register_blueprint(tenants)
app.register_blueprint(staff)


if __name__ == "__main__":
    app.run(debug="TRUE")
