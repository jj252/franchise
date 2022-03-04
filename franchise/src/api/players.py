from flask import Blueprint, jsonify, abort, request
from ..models import Player, db

bp = Blueprint('players', __name__, url_prefix='/players')

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    players = Player.query.all()  # ORM performs SELECT query
    
    result = []
    for t in players:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    player = Player.query.get_or_404(id)
    print(player.team.city)
    print(player.team_id)
    print(player.players_coach)
    for t in player.players_coach:
        print(t.name) # build list of Tweets as dictionaries
    return jsonify(player.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'name' not in request.json or 'work_position' not in request.json:
        return abort(400)
    
    u = Player(
        name=request.json['name'],
        work_position=request.json['work_position'],
        team_id=request.json['team_id'],
        status=request.json['status'],
        experience=request.json['experience']
        #stadium_id=request.json['stadium_id'],
        #admin_id=request.json['admin_id']
    )

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['PUT'])
def update(id:int):
    
    u = Player.query.get_or_404(id)
    
    # construct Tweet
    u2 = Player(
         name=request.json['name'],
         work_position=request.json['work_position'],
         status=request.json['status'],
         experience=request.json['experience']
    )
    
    u.name = u2.name
    u.work_position = u2.work_position
    u.status = u2.status
    u.experience = u2.experience
    
    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Player.query.get_or_404(id)
    try:
        db.session.delete(t)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>/team_for_players', methods=['GET'])
def team_for_players(id: int):
    players = Player.query.get_or_404(id)  # ORM performs SELECT query

    result = []
    result.append(players.team.serialize())
    result.append(players.name)
    print(players.team.city)

    return jsonify(result)

@bp.route('/<int:id>/coach_for_players', methods=['GET'])
def coach_for_players(id: int):
    players = Player.query.get_or_404(id)  # ORM performs SELECT query

    result = []
    #result.append(players.team.serialize())
    print(players.players_coach)
    for t in players.players_coach:
        result.append(t.serialize())
        
    return jsonify(result)

@bp.route('/<int:id>/equipment_for_players', methods=['GET'])
def equipment_for_players(id: int):
    players = Player.query.get_or_404(id)  # ORM performs SELECT query

    result = []
    #result.append(players.team.serialize())
    print(players.equipment)
    for t in players.equipment:
        result.append(t.serialize())
        result.append(players.name)
    return jsonify(result)