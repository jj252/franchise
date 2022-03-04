from flask import Blueprint, jsonify, abort, request
from ..models import Admin, db

bp = Blueprint('admins', __name__, url_prefix='/admins')

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    admins = Admin.query.all()  # ORM performs SELECT query
    result = []
    for t in admins:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('/<int:id>/team_for_admin', methods=['GET'])
def team_for_admin(id: int):
    admins = Admin.query.get_or_404(id)  # ORM performs SELECT query
    #tweets2 = Tweet.likes.query.all()  # ORM performs SELECT query
    print(admins.team)
    #db.session.add(tweets)  # prepare CREATE statement
    #db.session.commit()  # execute CREATE statement
    #print(users.tweets)
    result = []
    for t in admins.team:
        print(t.city)
        result.append(t.serialize())
        result.append(admins.name)
    return jsonify(result)

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'name' not in request.json or 'work_position' not in request.json:
        return abort(400)
    
    u = Admin(
        name=request.json['name'],
        work_position=request.json['work_position']
        #stadium_id=request.json['stadium_id'],
        #admin_id=request.json['admin_id']
    )

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())