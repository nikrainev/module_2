from datetime import datetime

from bson import ObjectId

from src.datasource.schemes.Transcription import Transcription
from src.db import get_db
from src.datasource.collection_names import transcriptionCollection

def create_transcribtion(name:str, owner_user_id:str, category_id:str, file_name:str):
    db = get_db()
    category_doc = Transcription(
        name=name,
        owner_user_id=owner_user_id,
        category_id=category_id,
        file_name=file_name
    )

    return db[transcriptionCollection].insert_one(category_doc)

def set_file_to_transcribtion(id:str, fileSrc:str):
    db = get_db()

    db[transcriptionCollection].update_one(
        {"_id": ObjectId(id)},
        {"$set": {"status": "fileUploaded", "fileSrc": fileSrc}}
    )

def set_text_to_transcribtion(id:str, text:str):
    db = get_db()

    db[transcriptionCollection].update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "status": "completed",
            "text": text,
            "completedAt": datetime.now()
        }},
    )