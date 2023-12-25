from datetime import datetime
from bson.objectid import ObjectId

def Category(name:str, owner_user_id:str):
    return {
        'createdAt': datetime.now(),
        'name': name,
        'ownerUser': ObjectId(owner_user_id)
    }