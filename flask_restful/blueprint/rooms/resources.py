import json
from flask_restful import Resource, request, marshal_with, fields, reqparse, current_app
from models import Rooms
from db import db

rooms_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Float}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("room_num", type=int, help="Custom error + default: {error_msg}")
parser.add_argument("room_status", type=str, choices=["Free", "Busy"], help="Custom error + default: {error_msg}")


class GetRooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        room_number = parser.parse_args().get("room_num")
        room_status = parser.parse_args().get("room_status")
        if room_number:
            room = Rooms.query.filter(
                Rooms.number == room_number).first()
            return room, 200
        if room_status:
            room = Rooms.query.filter(
                Rooms.status == room_status).all()
            return room, 200
        return Rooms.query.all(), 200

    @marshal_with(rooms_structure)
    def post(self):
        data = json.loads(request.data)
        if Rooms.query.filter(Rooms.number == data.get("number")).first():
            # return Response("This room exists", 404)
            return current_app.logger.info("This room exists"), 404
        else:
            room = Rooms(**data)
            try:
                db.session.add(room)
                db.session.commit()
            except ConnectionError:
                return "Connection error", 404
            return room, 200

    @marshal_with(rooms_structure)
    def patch(self):
        data = json.loads(request.data)
        room_number = data.get("number")
        room = Rooms.query.get(room_number)
        if room:
            room.status = data.get("status")
            try:
                db.session.commit()
                return room
            except ConnectionError:
                return "Error"
        return "Sorry, such room doesn't exist", 404

    def delete(self):
        room_number = parser.parse_args().get("room_num")
        room = Rooms.query.get(room_number)
        if room_number:
            try:
                db.session.delete(room)
                db.session.commit()
            except ConnectionError:
                return "Error", 404
            return "Room deleted", 200
        else:
            return "Sorry, such room doesn't exist", 404





