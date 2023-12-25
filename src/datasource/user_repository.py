from src.datasource.schemes.User import User, CreateUserArgs
from src.db import get_db
from src.datasource.collection_names import userCollection
from bson.objectid import ObjectId

def create_user(creatArgs:CreateUserArgs):
    db = get_db()
    user_doc = User(creatArgs)

    db[userCollection].insert_one(user_doc)

    return find_user_by_username(creatArgs.username)

def find_user_by_username(username):
    db = get_db()
    return list(db[userCollection].find({ 'username': username }, {}))

def find_user_by_id(id):
    db = get_db()
    return list(db[userCollection].find({ '_id': ObjectId(id) }, {}))