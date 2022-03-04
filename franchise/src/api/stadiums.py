from flask import Blueprint, jsonify, abort, request
from ..models import Stadium, db

bp = Blueprint('stadiums', __name__, url_prefix='/stadiums')

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    stadiums = Stadium.query.all()  # ORM performs SELECT query
    result = []
    for t in stadiums:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'name' not in request.json or 'capacity' not in request.json:
        return abort(400)
    
    u = Stadium(
        name=request.json['name'],
        capacity=request.json['capacity']
        #stadium_id=request.json['stadium_id'],
        #admin_id=request.json['admin_id']
    )

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())

@bp.route('/<int:id>/stadium_for_team', methods=['GET'])
def stadium_for_team(id: int):
    stadiums = Stadium.query.get_or_404(id)  # ORM performs SELECT query
    print(stadiums.teams)
    result = []
    for t in stadiums.teams:
        result.append(t.serialize())  # build list of Tweets as dictionaries
        result.append(stadiums.name)
    return jsonify(result)  # return JSON response
    #result.append(stadiums.teams.serialize())
    