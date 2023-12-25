from datetime import datetime
from bson.objectid import ObjectId

def Transcription(name:str, owner_user_id:str, category_id:str, file_name:str) -> dict:
    return {
        'createdAt': datetime.now(),
        'completedAt': None,
        'status': 'init',
        'fileSrc': None,
        'text': None,
        'fileName': file_name,
        'name': name,
        'ownerUser': ObjectId(owner_user_id),
        'category': ObjectId(category_id)
    }