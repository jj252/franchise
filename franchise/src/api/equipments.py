from flask import Blueprint, jsonify, abort, request
from ..models import Equipment, db

bp = Blueprint('equipments', __name__, url_prefix='/equipments')

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    teams = Equipment.query.all()  # ORM performs SELECT query
    result = []
    for t in teams:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Equipment.query.get_or_404(id)
    return jsonify(t.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'helmet_size' not in request.json or 'shoulder_size' not in request.json:
        return abort(400)
    
    u = Equipment(
        helmet_size=request.json['helmet_size'],
        body_size=request.json['body_size'],
        shoulder_size=request.json['shoulder_size'],
        leg_size=request.json['leg_size'],
        player_id=request.json['player_id']
    )

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())

@bp.route('/<int:id>/players_equipment', methods=['GET'])
def players_equipment(id: int):
    equipments = Equipment.query.get_or_404(id)  # ORM performs SELECT query

    result = []
    result.append(equipments.player.serialize())
    result.append(equipments.serialize())
    
    return jsonify(result)  # return JSON response

