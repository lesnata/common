from flask import Blueprint
from flask_restful import Api
from blueprint.rooms.resources import GetRooms

rooms = Blueprint("rooms", __name__)
api = Api(rooms)

api.add_resource(GetRooms, '/rooms')
