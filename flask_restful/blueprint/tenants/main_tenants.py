from flask import Blueprint
from flask_restful import Api
from blueprint.tenants.resources_tenants import GetTenants

tenants = Blueprint("tenants", __name__)
api = Api(tenants)

api.add_resource(GetTenants, '/tenants')
