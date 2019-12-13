from flask import Blueprint
from flask_restful import Api
from blueprint.staff.resources_staff import GetStaff

staff = Blueprint("staff", __name__)
api = Api(staff)

api.add_resource(GetStaff, '/staff')
