import json
from flask import Response
from flask_restful import Resource, request, marshal_with, fields, reqparse
from utility import get_data, add_data

staff = get_data("blueprint/staff/staff.json")

staff_structure = {
    "name": fields.String,
    "passport": fields.Integer,
    "position": fields.String,
    "salary": fields.Float}


class Staff:
    def __init__(self, name, passport, position, salary):
        self.name = name
        self.passport = passport
        self.position = position
        self.salary = salary

    def make_dict(self):
        return {"name": self.name,
                "passport": self.passport,
                "position": self.position,
                "salary": self.salary,
                }


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("passport", type=int, help="Custom error + default: {error_msg}")


class GetStaff(Resource):
    @marshal_with(staff_structure)
    def get(self):
            args = parser.parse_args()
            if args["passport"]:
                for i in staff:
                    if args["passport"] == i["passport"]:
                        return i
            else:
                return staff

    def post(self):
        data = request.json
        for person in staff:
            if person.get("passport") == data["passport"]:
                return Response("Person with passport #{} exists".format(data["passport"]), 200)
            else:
                new_stuff = Staff(data.get("name"), data.get("passport"),
                                  data.get("position"), data.get("salary"))
                staff.append(new_stuff.make_dict())
                add_data(staff, "blueprint/staff/staff.json")
                return Response("Person with passport #{} added".format(data.get("passport")), 200)

    def patch(self):
        data = request.json
        for person in staff:
            if person.get("passport") == data["passport"]:
                person.update(data)
            add_data(staff, "blueprint/staff/staff.json")
        return Response("Person with passport #{} updated".format(data.get("passport")), 200)

    def delete(self):
        args = parser.parse_args()
        for person in range(len(staff)):
            if args["passport"] == staff[person].get("passport"):
                del staff[person]
                break
            else:
                print("Sorry, no such staff found")
        add_data(staff, "blueprint/staff/staff.json")
        return Response("Person with passport #{} is successfully deleted".format(args["passport"]), 200)



