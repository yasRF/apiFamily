"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Family
from api.utils import generate_sitemap, APIException


api = Blueprint('api', __name__)



@api.route('/Family', methods=['GET'])
def get_members():
    Members = Family.query.all()
    result = [element.serialize() for element in Members]
    response_body = {
        "message": "lista familiar"
    }

    return jsonify(result), 200
    
@api.route('/Family/<int:family_id>', methods=['GET'])
def get_members_id(family_id):
    GetMember = Family.query.get(family_id)
    result = GetMember.serialize()
    response_body = {"msg": "un familiar"}
    return jsonify(result), 200


@api.route('/Family', methods=['POST'])
def create_members():
    data = request.data
    data = json.loads(data)

    Member = Family(
        name= data["name"],
        lastname = data ["lastname"],
        years = data["years"])
    db.session.add(Member)
    db.session.commit()

    response_body = {
        "message": "Creado!"
    }
    return jsonify(Member.serialize())

@api.route('/Family', methods=['DELETE'])
def delete_members():
    data = request.data
    data = json.loads(data)

    memberDel = Family(
    name= data["name"],
    lastname = data ["lastname"],
    years = data["years"])

    db.session.delete(memberDel)
    db.session.commit()
    

    response_body = {
        "message": "borrado!"
    }

    return jsonify(memberDel), 200
