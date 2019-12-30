from flask import Blueprint
from flask_restful import Api
from blueprint.rooms_tenants.resources import GetRoomsTenants

rooms_tenants = Blueprint("rooms_tenants", __name__)
api = Api(rooms_tenants)

api.add_resource(GetRoomsTenants, "/tenant/<tenant_id>/rooms")
