import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships

class Team(db.Model):

    def __init__(self, city: str, symbol: str):
            self.city = city
            self.symbol = symbol
    def serialize(self):
            return {
                'id': self.id,
                'city': self.city,
                'symbol': self.symbol
            }

    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(128), unique=True, nullable=False)
    symbol = db.Column(db.String(128), nullable=False)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadiums.id'), nullable=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'), nullable=True)
    coaches = db.relationship('Coach', backref='team', cascade="all,delete")
    players = db.relationship('Player', backref='team', cascade="all,delete")
    #stadiums = db.relationship('Stadium', backref='team', cascade="all,delete")
    #tweets = db.relationship('Tweet', backref='user', cascade="all,delete")

class Stadium(db.Model):

    def __init__(self, name: str, capacity: int):
            self.name = name
            self.capacity = capacity
    def serialize(self):
            return {
                'id': self.id,
                'name': self.name,
                'merchandise': self.merchandise,
                'menu': self.menu,
                'capacity': self.capacity
            }

    __tablename__ = 'stadiums'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    merchandise = db.Column(db.String(128), nullable=True)
    menu = db.Column(db.String(128), nullable=True)
    capacity = db.Column(db.Integer, nullable=False)
    teams = db.relationship('Team', backref='stadium', cascade="all,delete")
    #team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)

class Admin(db.Model):

    def __init__(self, name: str, work_position: str):
            self.name = name
            self.work_position = work_position
    def serialize(self):
            return {
                'id': self.id,
                'name': self.name,
                'work_position': self.work_position
            }

    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    work_position = db.Column(db.String(128), nullable=False)
    team = db.relationship('Team', backref='admin', cascade="all,delete")
    #work_position2 = db.Column(db.String(128), nullable=True)
    #team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)

manages_table = db.Table(
    'manages',
    db.Column(
        'coach_id', db.Integer,
        db.ForeignKey('coaches.id'),
        primary_key=True
    ),
    db.Column(
        'player_id', db.Integer,
        db.ForeignKey('players.id'),
        primary_key=True
    )
)

class Coach(db.Model):

    def __init__(self, name: str, work_position: str):
            self.name = name
            #self.salary = salary
            self.work_position = work_position
            
    def serialize(self):
            return {
                'id': self.id,
                'name': self.name,
                'work_position': self.work_position
                
                #'salary': self.salary,
            }

    __tablename__ = 'coaches'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    work_position = db.Column(db.String(128), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    players_coach = db.relationship(
        'Player', secondary=manages_table,
        lazy='subquery',
        backref=db.backref('manages_table', lazy=True)
    )
    #coaches = db.relationship('Player', backref='coaches', cascade="all,delete")
    



class Player(db.Model):

    def __init__(self, name: str, work_position: str, status: str, experience: str, team_id: int):
            self.name = name
            self.work_position = work_position
            self.status = status,
            self.experience = experience,
            self.team_id = team_id
    def serialize(self):
            return {
                'id': self.id,
                'name': self.name,
                'work_position': self.work_position,
                'status': self.status,
                'experience': self.experience,
                'team_id': self.team_id
            }

    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    work_position = db.Column(db.String(128), nullable=True)
    status = db.Column(db.String(128), nullable=False)
    experience = db.Column(db.String(128), nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    equipment = db.relationship('Equipment', backref='player', cascade="all,delete")
    players_coach = db.relationship(
        'Coach', secondary=manages_table,
        lazy='subquery',
        backref=db.backref('manages_table', lazy=True)
    )
    #tweets = db.relationship('Tweet', backref='user', cascade="all,delete")


class Equipment(db.Model):

    def __init__(self, helmet_size: str, shoulder_size: str, body_size: str, leg_size: str, player_id: int):
            self.helmet_size = helmet_size
            self.shoulder_size = shoulder_size
            self.body_size = body_size
            self.leg_size = leg_size
            self.player_id = player_id
    def serialize(self):
            return {
                'id': self.id,
                'helmet_size': self.helmet_size,
                'shoulder_size': self.shoulder_size,
                'body_size': self.body_size,
                'leg_size': self.leg_size,
                'player_id': self.player_id
            }

    __tablename__ = 'equipments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    helmet_size = db.Column(db.String(128), nullable=False)
    shoulder_size = db.Column(db.String(128), nullable=False)
    body_size = db.Column(db.String(128), nullable=False)
    leg_size = db.Column(db.String(128), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=True)

    
    