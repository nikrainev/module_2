from bson import ObjectId

from src.datasource.schemes.Category import Category
from src.db import get_db
from src.datasource.collection_names import categoryCollection

def create_category(name:str, owner_user_id: str):
    db = get_db()
    category_doc = Category(name=name, owner_user_id=owner_user_id)

    db[categoryCollection].insert_one(category_doc )

def find_category_by_id(id):
    db = get_db()
    return list(db[categoryCollection].find({ '_id': ObjectId(id) }, {}))

def get_user_categories(userId:str):
    db = get_db()
    return list(db[categoryCollection].aggregate([
    {
        '$match': {
            'ownerUser': ObjectId(userId)
        }
    }, {
        '$lookup': {
            'from': 'transcription',
            'localField': '_id',
            'foreignField': 'category',
            'as': 'transciptions'
        }
    }, {
        '$project': {
            '_id': 0,
            'ownerUser': 0,
            'transciptions._id': 0,
            'transciptions.ownerUser': 0,
            'transciptions.category': 0
        }
    }
]))