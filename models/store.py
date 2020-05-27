# Internal presentation of what_an_Item_is and how_it_looks_like?...
# import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')     # a_list of ItemModel (Many to one relation) (Many items for one store)
                                                            # lazy='dynamic' is_to not_to create object for every item in tables in DB 

    def __init__(self, name):                                # there is_no "id" parameter, it won't be used
        self.name = name
    
    def json(self):                                                     # to return a_basic_json_representation(ItemModel)..i.e.item
        return {'name': self.name, 
                'items': [item.json() for item in self.items.all()]}    # seld.items is no longer raise a_list_of items (lazy='dynamic')
                                                                        # now, it's a query builder

    @classmethod                                                        # should_be_a_classMethod BCZ it_returns an_object_of_type_"ItemModel"
    def find_by_name(cls, name):                                        #       as supposed to a DICTIONARY
        
        # returns the "ItemModel_object"
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):                                               # contains_for_both_INSERT_and_UPDATE
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
