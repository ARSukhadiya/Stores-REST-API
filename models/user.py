import sqlite3
from db import db

class UserModel(db.Model):                                  # makes aware to SQLAlchemy to mapp "UserModel" object class with DB
    __tablename__ = 'users'

    # "id" will auto-incrementingly assign to DB, i.e. it doesn't need to pass manually.
    id = db.Column(db.Integer, primary_key=True)            # tell_alchemy_that a_column that a_model_is_going_to_have
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.something = "hi"                               # will not be saved in DB, WON'T_give_any_ERROR

    def save_to_db(self):
        db.session.add(self)            #  db.session.delete(self)...to delete
        db.session.commit()

    @classmethod
    def find_by_username(cls, username): 
        return cls.query.filter_by(username= username).first()
                                                                # connection = sqlite3.connect('data.db') 
                                                                # cursor = connection.cursor() 

                                                                # query = "SELECT * FROM users WHERE username=?" 
                                                                # result = cursor.execute(query, (username,))         # parameters have to be in_a_form_of_TUPLE (___,)
                                                                # row = result.fetchone() 
                                                                # if row: 
                                                                #     user = cls(*row)             # row[0], row[1], row[2]
                                                                # else: 
                                                                #     user = None 
                                                                # connection.close() 
                                                                # return user 

    @classmethod 
    def find_by_id(cls, _id): 
        return cls.query.filter_by(id= _id).first()
                                                                # connection = sqlite3.connect('data.db') 
                                                                # cursor = connection.cursor() 

                                                                # query = "SELECT * FROM users WHERE id=?" 
                                                                # result = cursor.execute(query, (_id,))         # parameters have to be in_a_form_of_TUPLE (___,)
                                                                # row = result.fetchone() 
                                                                # if row: 
                                                                #     user = cls(*row)            # row[0], row[1], row[2]
                                                                # else: 
                                                                #     user = None 
                                                                # connection.close() 
                                                                # return user 
                                                                    