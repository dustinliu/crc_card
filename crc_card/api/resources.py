
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

from crc_card import db
from crc_card.core.board import Board

board_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'created_time': fields.DateTime(dt_format='iso8601'),
    'updated_time': fields.DateTime(dt_format='iso8601'),
}

card_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'created_time': fields.DateTime(dt_format='iso8601'),
    'updated_time': fields.DateTime(dt_format='iso8601'),
}

class BoardResource(Resource):
    @marshal_with(board_fields)
    def get(self, id):
        board = Board.query.get(id)
        if not board:
            abort(404)

        return board, 200

    @marshal_with(board_fields)
    def delete(self, id):
        board = Board.query.get(id)
        if board is None:
            abort(404)

        db.session.delete(board)
        db.session.commit()
        return board, 200

class BoardListResource(Resource):
    @marshal_with(board_fields)
    def get(self):
        return Board.query.all()

    @marshal_with(board_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="Name cannot be blank!")
        parser.add_argument('description')
        args = parser.parse_args()
        return Board.create(args.name, args.description), 201


class CardResource(Resource):
    @marshal_with(card_fields)
    def get(self, id):
        board = Board.query.get(id)
        if not board:
            abort(404)

        return board, 200

    @marshal_with(board_fields)
    def delete(self, id):
        board = Board.query.get(id)
        if board is None:
            abort(404)

        db.session.delete(board)
        db.session.commit()
        return board, 200



api_board = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_board)
api.add_resource(BoardResource, '/board/<int:id>')
api.add_resource(BoardListResource, '/board')
