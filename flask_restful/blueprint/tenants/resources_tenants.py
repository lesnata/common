import json
from flask_restful import Resource, request, marshal_with, fields, reqparse, current_app
from models import Tenants
from db import db

tenants_structure = {
    "name": fields.String,
    "passport": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "city": fields.String,
    "address": fields.String}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("passport", type=str, help="Custom error + default: {error_msg}")


class GetTenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        passport_no = parser.parse_args().get("passport")
        if passport_no:
            tenant = Tenants.query.filter(
                Tenants.passport == passport_no).first()
            return tenant, 200
        return Tenants.query.all(), 200

    @marshal_with(tenants_structure)
    def post(self):
        data = request.json
        tenant = data.get("passport")
        if Tenants.query.filter(Tenants.passport == tenant).first():
            return current_app.logger.info("This tenant exists"), 404
        new_tenant = Tenants(**data)
        try:
            db.session.add(new_tenant)
            db.session.commit()
        except ConnectionError:
            return "Connection error", 404
        return new_tenant

    @marshal_with(tenants_structure)
    def put(self):
        try:
            data = request.json
            tenant_pass = data.get("passport")
            tenant = Tenants.query.get(tenant_pass)
            for key, value in data.items():
                setattr(tenant, key, value)
                db.session.commit()
            return tenant
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when updated staff with following error - {error}"

    def delete(self):
        passport_no = parser.parse_args().get("passport")
        tenant = Tenants.query.get(passport_no)
        if tenant:
            try:
                db.session.delete(tenant)
                db.session.commit()
                return f"Tenant with {passport_no} passport number is deleted", 200
            except (ValueError, KeyError, TypeError) as error:
                return f"You have an error: {error}"
        return "No tenant found", 404


