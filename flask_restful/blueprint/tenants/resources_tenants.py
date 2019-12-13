import json
from flask import Response
from flask_restful import Resource, request, marshal_with, fields, reqparse, marshal
from utility import get_data, add_data

tenants = get_data("blueprint/tenants/tenants.json")

address_structure = {
    "city": fields.String,
    "street": fields.String,
}

tenants_structure = {
    "name": fields.String,
    "passport": fields.Integer,
    "age": fields.Integer,
    "sex": fields.String,
    "address": fields.Nested(address_structure),
    "room": fields.Integer}


class Tenants:
    def __init__(self, name, passport, age, sex, city, street, room):
        self.name = name
        self.passport = passport
        self.age = age
        self.sex = sex
        self.address = {"city": city, "street": street}
        self.room = room

    def make_dict(self):
        return {"name": self.name,
                "passport": self.passport,
                "age": self.age,
                "sex": self.sex,
                "address": self.address,
                "room": self.room,
                }


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("passport", type=int, help="Custom error + default: {error_msg}")


class GetTenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
            args = parser.parse_args()
            if args["passport"]:
                for i in tenants:
                    if args["passport"] == i["passport"]:
                        return i
                    else:
                        Response("No tenant with passport {} found".format(args["passport"]), 200)
            else:
                return tenants

    def post(self):
        data = request.json
        for tenant in tenants:
            if tenant.get("passport") == data["passport"]:
                return Response("{} tenant exists".format(data["passport"]), 200)
            else:
                new_tenant = Tenants(data.get("name"), data.get("passport"),
                                     data.get("age"), data.get("sex"), data.get("city"),
                                     data.get("street"), data.get("room"))
                tenants.append(new_tenant.make_dict())
                add_data(tenants, "blueprint/tenants/tenants.json")
                return Response("New tenant with passport #{} is added".format(data.get("passport")), 200)

    def patch(self):
        data = request.json
        for tenant in tenants:
            if tenant.get("passport") == data["passport"]:
                tenant.update(data)
            add_data(tenants, "blueprint/tenants/tenants.json")
        return Response("Tenant info with {} passport # is updated".format(data.get("passport")), 200)

    def delete(self):
        args = parser.parse_args()
        for tenant in range(len(tenants)):
            if args["passport"] == tenants[tenant].get("passport"):
                del tenants[tenant]
                break
            else:
                print("Sorry, no such tenant found")
        add_data(tenants, "blueprint/tenants/tenants.json")
        return Response("{} tenant data is successfully deleted".format(args["passport"]), 200)



