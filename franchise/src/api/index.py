from flask import Blueprint, jsonify, abort, request, render_template
from ..models import Player, db


bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    
    return render_template('index.html')