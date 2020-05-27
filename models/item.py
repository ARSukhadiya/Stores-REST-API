# Internal presentation of what_an_Item_is and how_it_looks_like?...
# import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))    # set foreign_key of id(stores) table 
    store = db.relationship('StoreModel')                           # works as a JOIN in SQLAlchemy

    def __init__(self, name, price, store_id):                      # there is_no "id" parameter, it won't be used
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):                                                 # to return a_basic_json_representation(ItemModel)..i.e.item
        return {'name': self.name, 'price': self.price}             # that_is a_dictionary representing_an_item

    @classmethod                                                    # should_be_a_classMethod BCZ it_returns an_object_of_type_"ItemModel"
    def find_by_name(cls, name):                                    #       as supposed to a DICTIONARY
        
        # returns the "ItemModel_object"
        # return ItemModel.query.filter_by(name=name).first()         # SELEST * FROM items WHERE name=name LIMIT_1
                                                #/.filetr_by(id=1)
        return cls.query.filter_by(name=name).first()
                                                    # connection = sqlite3.connect('data.db')

                                                    # cursor = connection.cursor()
                                                    # query = "SELECT * FROM items WHERE name=?"
                                                    # result = cursor.execute(query, (name,))
                                                    # row = result.fetchone()
                                                    # connection.close()
                                                    
                                                    # if row:
                                                    #     # return {'item': {'name': row[0], 'price': row[1]}}    # returns a Dictionary
                                                    #     return cls(*row)            # cls(row[0], row[1])       # return an_object_of_type_"ItemModel" instead_of_dictionary With_arg_unpacking

                                                # def insert(self):                                               # pass "item" as_it_self as_an_argument_of_function_of_ItemModel
                                                    # connection = sqlite3.connect('data.db')
                                                    # cursor = connection.cursor()

                                                    # query = "INSERT INTO items VALUES (?, ?)"
                                                    # # cursor.execute(query, (item['name'], item['price']))
                                                    # cursor.execute(query, (self.name, self.price))
                                                    
                                                    # connection.commit()
                                                    # connection.close()
    
    def save_to_db(self):                                             # contains_for_both_INSERT_and_UPDATE
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

                                                # def update(self):                       
                                                #     connection = sqlite3.connect('data.db')
                                                #     cursor = connection.cursor()
                                                #     # data = self.parser.parse_args()

                                                #     # item = cls.find_by_name(item['name'])

                                                #     query = "UPDATE items SET price=? WHERE name=?"
                                                #     cursor.execute(query, (self.name, self.price))

                                                #     connection.commit()
                                                #     connection.close()

                                                #     return {'message': 'Item deleted'}

    