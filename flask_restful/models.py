from db import db


staffs_works = db.Table(
    'staffs_work',
    db.Column('staff_id', db.String, db.ForeignKey('staff_table.passport')),
    db.Column('room_number', db.Integer, db.ForeignKey('rooms_table.number'))
)


class Rooms(db.Model):
    __tablename__ = "rooms_table"
    number = db.Column(db.Integer, primary_key=True, unique=True)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer)
    tenant_id = db.Column(db.String, db.ForeignKey('tenants.passport'))


class Staff(db.Model):
    __tablename__ = "staff_table"
    passport = db.Column(db.String, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    works = db.relationship('Rooms',  secondary=staffs_works, backref='staff_reference', lazy=True)


class Tenants(db.Model):

    passport = db.Column(db.String, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    rooms = db.relationship('Rooms', backref='tenant_ref', lazy=True)

