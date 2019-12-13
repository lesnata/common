import json
from flask import Response
from flask_restful import Resource, request, marshal_with, fields, reqparse, marshal
from utility import get_data, add_data

rooms = get_data("blueprint/rooms/rooms.json")

rooms_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Float}


class Rooms:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price

    def make_dict(self):
        return {"number": self.number,
                "level": self.level,
                "status": self.status,
                "price": self.price,
                }


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("id", type=int, help="Custom error + default: {error_msg}")
parser.add_argument("status", type=str, choices=["Free", "Busy"], help="Custom error + default: {error_msg}")


class GetRooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
            args = parser.parse_args()
            if args["id"]:
                for i in rooms:
                    if args["id"] == i["number"]:
                        result = Rooms(i["number"], i["level"], i["status"], i["price"])
                        return result
            else:
                if args.get("status"):
                    return [Rooms(elem["number"], elem["level"], elem["status"], elem["price"])
                            for elem in rooms if args["status"] == elem["status"]]
                return rooms

    def post(self):
        data = request.json
        for room in rooms:
            if room.get("number") == data["number"]:
                return Response("{} room exists".format(data["number"]), 200)
            else:
                new_room = Rooms(data.get("number"), data.get("level"),
                                 data.get("status"), data.get("price"))
                rooms.append(new_room.make_dict())
                add_data(rooms, "blueprint/rooms/rooms.json")
                return Response("New {} room added".format(data.get("number")), 200)
                    # marshal(rooms, rooms_structure)

    def patch(self):
        data = request.json
        for room in rooms:
            if room.get("number") == data["number"]:
                room.update(data)
            add_data(rooms, "blueprint/rooms/rooms.json")
        return Response("{} room info updated".format(data.get("number")), 200)

    def delete(self):
        args = parser.parse_args()
        for room in range(len(rooms)):
            if args["id"] == rooms[room].get("number"):
                del rooms[room]
                break
            else:
                print("Sorry, no such room found")
        add_data(rooms, "blueprint/rooms/rooms.json")
        return Response("{} room is successfully deleted".format(args["id"]), 200)



