from flask import Blueprint, jsonify, abort, request
from ..models import Team, db

bp = Blueprint('teams', __name__, url_prefix='/teams')

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    teams = Team.query.all()  # ORM performs SELECT query
    result = []
    for t in teams:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Team.query.get_or_404(id)
    return jsonify(t.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'city' not in request.json or 'symbol' not in request.json:
        return abort(400)
    
    u = Team(
        city=request.json['city'],
        symbol=request.json['symbol'],
        #stadium_id=request.json['stadium_id'],
        #admin_id=request.json['admin_id']
    )

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Team.query.get_or_404(id)
    try:
        db.session.delete(t)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PUT'])
def update(id:int):
    
    u = Team.query.get_or_404(id)
    
    # construct Tweet
    u2 = Team(
         city=request.json['city'],
         symbol=request.json['symbol']
    )
    
    u.city = u2.city
    u.symbol = u2.symbol
    
    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())

@bp.route('/<int:id>/players_in_team', methods=['GET'])
def players_in_team(id: int):
    teams = Team.query.get_or_404(id)  # ORM performs SELECT query
    #tweets2 = Tweet.likes.query.all()  # ORM performs SELECT query
    print(teams.city)
    print(teams.players[0])
    #db.session.add(tweets)  # prepare CREATE statement
    #db.session.commit()  # execute CREATE statement
    #print(users.tweets)
    result = []
    for t in teams.players:
        result.append(t.serialize())
        result.append(teams.city)
    return jsonify(result)

@bp.route('/<int:id>/coaches_in_team', methods=['GET'])
def coaches_in_team(id: int):
    teams = Team.query.get_or_404(id)  # ORM performs SELECT query
    #tweets2 = Tweet.likes.query.all()  # ORM performs SELECT query
    print(teams.city)
    print(teams.coaches[0])
    print(teams.stadium.name)
    print(teams.players[0])
    #print(coaches.stadiums)
    #db.session.add(tweets)  # prepare CREATE statement
    #db.session.commit()  # execute CREATE statement
    #print(users.tweets)
    result = []
    for t in teams.coaches:
        result.append(t.serialize())
        result.append(teams.city)
    return jsonify(result)

@bp.route('/<int:id>/stadium_belongs_to_team', methods=['GET'])
def stadium_belongs_to_team(id: int):
    teams = Team.query.get_or_404(id)  # ORM performs SELECT query
    #tweets2 = Tweet.likes.query.all()  # ORM performs SELECT query
    print(teams.city)
    print(teams.coaches[0])
    print(teams.stadium.name)
    print(teams.players[0])
    #print(coaches.stadiums)
    #db.session.add(tweets)  # prepare CREATE statement
    #db.session.commit()  # execute CREATE statement
    #print(users.tweets)
    result = []
    result.append(teams.stadium.serialize())
    result.append(teams.city)

    #for t in teams.stadium:
        
    return jsonify(result)

@bp.route('/<int:id>/admins_for_team', methods=['GET'])
def admins_for_team(id: int):
    teams = Team.query.get_or_404(id)  # ORM performs SELECT query
    #tweets2 = Tweet.likes.query.all()  # ORM performs SELECT query
    print(teams.city)
    print(teams.coaches[0])
    print(teams.stadium.name)
    print(teams.players[0])
    #print(coaches.stadiums)
    #db.session.add(tweets)  # prepare CREATE statement
    #db.session.commit()  # execute CREATE statement
    #print(users.tweets)
    result = []
    result.append(teams.admin.serialize())
    result.append(teams.city)

    #for t in teams.stadium:
        
    return jsonify(result)

