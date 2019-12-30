import json
from flask_restful import Resource, request, marshal_with, fields, reqparse, current_app
from models import Staff
from db import db

staff_structure = {
    "name": fields.String,
    "passport": fields.String,
    "position": fields.String,
    "salary": fields.Integer}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("passport", type=str, help="Custom error + default: {error_msg}")


class GetStaff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        passport_no = parser.parse_args().get("passport")
        if passport_no:
            staff_employee = Staff.query.filter(
                Staff.passport == passport_no).first()
            return staff_employee, 200
        return Staff.query.all(), 200

    @marshal_with(staff_structure)
    def post(self):
        data = request.json
        staff_employee = data.get("passport")
        if Staff.query.filter(Staff.passport == staff_employee).first():
            return current_app.logger.info("This employee exists"), 404
        new_employee = Staff(**data)
        try:
            db.session.add(new_employee)
            db.session.commit()
        except ConnectionError:
            return "Connection error", 404
        return new_employee

    @marshal_with(staff_structure)
    def put(self):
        try:
            data = request.json
            staff_employee = data.get("passport")
            staff = Staff.query.get(staff_employee)
            for key, value in data.items():
                setattr(staff, key, value)
                db.session.commit()
            return staff
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when updated staff with following error - {error}"

    def delete(self):
        passport_no = parser.parse_args().get("passport")
        staff_employee = Staff.query.get(passport_no)
        if staff_employee:
            try:
                db.session.delete(staff_employee)
                db.session.commit()
                return f"Staff employee with {passport_no} passport number is deleted", 200
            except (ValueError, KeyError, TypeError) as error:
                return f"You have an error: {error}"
        return "No employee found", 404

