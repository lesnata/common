import json
from flask_restful import Resource, marshal_with, fields, reqparse
from models import Rooms, Staff
from db import db

rooms_staff_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String
}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("room", type=str, help="Custom error + default: {error_msg}")
parser.add_argument("staff_id", required=True, type=str, help="Custom error + default: {error_msg}")


class GetRoomsStaff(Resource):
    @marshal_with(rooms_staff_structure)
    def get(self):
        try:
            staff_id = parser.parse_args().get("staff_id")
            staff = Staff.query.get(staff_id)
            return staff.works
        except (ValueError, KeyError, TypeError) as error:
            return f"Error when getting rooms of tenant - {error}"

    @marshal_with(rooms_staff_structure)
    def post(self):
        try:
            staff_id = parser.parse_args().get("staff_id")
            room_no = parser.parse_args().get("room")
            staff = Staff.query.get(staff_id)
            room = Rooms.query.filter_by(number=room_no).first()
            staff.works.append(room)
            db.session.commit()
            return staff.works

        except (ValueError, KeyError, TypeError) as error:
            return f"Error when getting rooms of tenant - {error}"

    def delete(self):
        try:
            room_no = parser.parse_args().get("room")
            staff_id = parser.parse_args().get("staff_id")
            room = Rooms.query.filter_by(number=room_no).first()
            staff = Staff.query.get(staff_id)
            staff.works.remove(room)
            db.session.commit()
            return f"Room number {room_no} was deleted from {staff_id} staff's list", 200
        except (ValueError, KeyError, TypeError) as error:
            return f"Error when deleting room from staff's list - {error}", 404

