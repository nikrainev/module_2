from src.datasource.category_repository import create_category, get_user_categories


def create_category_service(name:str, ownerUserId:str):
    create_category(name, ownerUserId)

def get_my_categories_service(token:str):
    return get_user_categories(token)