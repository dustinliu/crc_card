from flask_restful import abort
from sqlalchemy import UniqueConstraint, func, TIMESTAMP, ForeignKey

from crc_board import db

class Board(db.Model):
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256))
    created_time = db.Column(db.TIMESTAMP, server_default=func.now())
    updated_time = db.Column(db.TIMESTAMP, server_default=func.now(),
                            server_onupdate=func.current_timestamp())
    cards = db.relationship('Card')
    __table_args__ = (UniqueConstraint('name', name='uc_name'),)

    @staticmethod
    def create(name, description=None):
        board = Board()
        board.name = name
        if description is not None:
            board.description = description

        db.session.add(board)
        db.session.flush()
        db.session.commit()
        return board


class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    responsibilities = db.Column(db.CLOB)
    board_id = db.Column(db.INTEGER,
                         ForeignKey('boards.id',onupdate="CASCADE", ondelete="CASCADE"),
                         nullable=False
                         )
    created_time = db.Column(TIMESTAMP, server_default=func.now())
    updated_time = db.Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())
    __table_args__ = (UniqueConstraint('name', name='uc_name'),)