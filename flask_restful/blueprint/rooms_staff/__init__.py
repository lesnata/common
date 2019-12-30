from flask import Blueprint
from flask_restful import Api
from blueprint.rooms_staff.resources import GetRoomsStaff

rooms_staff = Blueprint("rooms_staff", __name__)
api = Api(rooms_staff)

api.add_resource(GetRoomsStaff, "/rooms_staff")

