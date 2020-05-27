import sqlite3 
from flask_restful import Resource, reqparse 
from flask_jwt import jwt_required 
from models.item import ItemModel 

class Item(Resource): 
    parser = reqparse.RequestParser()                                   # used to parse certain argument from json payload 
    parser.add_argument('price', 
        type = float,
        required = True,
        help = "This field cannot be left blank!"
    )
    parser.add_argument('store_id', 
        type = int,
        required = True,
        help = "Every item needs a store_id."
    ) 

    @jwt_required()                         # to authenticate before get item details
    def get(self, name): 
        item = ItemModel.find_by_name(name) 
        if item: 
            return item.json()              # because item represents an object_of_ItemModel
        return {'message': 'item not found'}, 404 

    def post(self, name): 
        if ItemModel.find_by_name(name):         # is not None:       # for no_duplication 
            return {'messgage': "An item with name {} already exists.".format(name)}, 400  # Request Error 

        data = Item.parser.parse_args()         # take passed parameters during request dispatch

        item = ItemModel(name, **data)          # item = ItemModel(name, data['price'], data['store_id'])     
        try:
            # ItemModel.insert(item)
            item.save_to_db()
        except:
            return {"message": "An error occured inserting the item."}, 500  # Internal Server Error

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": "Item deleted"}
                                                                # connection = sqlite3.connect('data.db')
                                                                # cursor = connection.cursor()

                                                                # query = "DELETE FROM items WHERE name=?"
                                                                # cursor.execute(query, (name,))

                                                                # connection.commit()
                                                                # connection.close()
                                                                # return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])
        
        if item is None:
            item = ItemModel(name, **data)
                                                                # try:
                                                                #     updated_item.insert()
                                                                #     # ItemModel.insert(updated_item)                                           
                                                                # except:
                                                                #     {"message": "An error occured inserting the item."}, 500
        else:
            item.price = data['price']
                                                                # try:
                                                                #     updated_item.update()
                                                                #     # ItemModel.update(updated_item)
                                                                # except:
                                                                #     {"message": "An error occured updating the item."}, 500
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}     # list_comprehension
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

                                                                # connecion = sqlite3.connect('data.db')
                                                                # cursor = connecion.cursor()

                                                                # query = "SELECT * FROM items"
                                                                # result = cursor.execute(query)
                                                                # items = result.fetchall()
                                                                # connecion.close()

                                                                # return {'items': items}