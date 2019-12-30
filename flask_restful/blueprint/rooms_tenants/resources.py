import json
from flask_restful import Resource, request, marshal_with, fields, reqparse, current_app
from models import Tenants, Rooms
from db import db

rooms_tenants_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String
}


class GetRoomsTenants(Resource):
    @marshal_with(rooms_tenants_structure)
    def get(self, tenant_id):
        try:
            tenant = Tenants.query.get(tenant_id)
            return tenant.rooms
        except (ValueError, KeyError, TypeError) as error:
            return f"Error when getting rooms of {tenant_id} - {error}"

    @marshal_with(rooms_tenants_structure)
    def post(self, tenant_id):
        try:
            data = request.json
            tenant = Tenants.query.get(tenant_id)
            room_number = data.get("number")
            room = Rooms.query.filter_by(number=room_number).first()
            room.status = data.get("status")
            tenant.rooms.append(room)
            db.session.commit()
            return tenant.rooms
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when got tenants rooms list with following error - {error}"

    def delete(self, tenant_id):
        try:
            data = request.json
            room_no = data.get("number")
            tenant = Tenants.query.get(tenant_id)
            room = Rooms.query.filter_by(number=room_no).first()
            tenant.rooms.remove(room)
            db.session.commit()
            return f"Room number {room_no} was deleted from {tenant_id} tenant's list", 200
        except (ValueError, KeyError, TypeError) as error:
            return f"Error when deleting from {tenant_id} tenant's list - {error}", 404

