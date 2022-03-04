from flask import Blueprint, jsonify, abort, request
from ..models import Coach, db

bp = Blueprint('coaches', __name__, url_prefix='/coaches')

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    coaches = Coach.query.all()  # ORM performs SELECT query
    result = []
    for t in coaches:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Coach.query.get_or_404(id)
    return jsonify(t.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'name' not in request.json or 'work_position' not in request.json:
        return abort(400)
    
    # user with id of user_id must exist
    #User.query.get_or_404(request.json['username'])

    # construct Tweet
    u = Coach(
        name=request.json['name'],
        work_position=request.json['work_position']
        #stadium_id=request.json['stadium_id'],
        #admin_id=request.json['admin_id']
    )

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Coach.query.get_or_404(id)
    try:
        db.session.delete(t)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PUT'])
def update(id:int):
    # req body must contain user_id and content
    #if 'user_id' not in request.json or 'content' not in request.json:
        #return abort(400)

    # user with id of user_id must exist
    #User.query.get_or_404(request.json[id])
    u = Coach.query.get_or_404(id)
    
    # construct Tweet
    u2 = Coach(
         name=request.json['name'],
         work_position=request.json['work_position']
    )
    
    u.name = u2.name
    u.work_position = u2.work_position
    
    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())

@bp.route('/<int:id>/team_for_coaches', methods=['GET'])
def team_for_coaches(id: int):
    coaches = Coach.query.get_or_404(id)  # ORM performs SELECT query

    result = []
    result.append(coaches.team.serialize())
    result.append(coaches.name)

    return jsonify(result)

@bp.route('/<int:id>/players_for_coach', methods=['GET'])
def players_for_coach(id: int):
    coaches = Coach.query.get_or_404(id)  # ORM performs SELECT query
    print(coaches.players_coach)
    result = []
    for t in coaches.players_coach:
        result.append(t.serialize())  # build list of Tweets as dictionaries
        result.append(coaches.name)
    return jsonify(result)  # return JSON response
    '''result = []
    result.append(coaches.team.serialize())
    result.append(coaches.name)

    return jsonify(result)'''


