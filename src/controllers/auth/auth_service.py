import configparser
import os

import ipinfo

from src.controllers.auth.request.create_user_request import CreateUserRequest
from src.datasource.user_repository import create_user, find_user_by_username, find_user_by_id
from src.datasource.schemes.User import CreateUserArgs

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

LOCAL_IP_ADDRESS = '127.0.0.1'

def create_user_service(req:CreateUserRequest):
    existedUser = find_user_by_username(req.username)

    if (len(existedUser) > 0):
        return {
            'error': "User already exists"
        }

    handler = ipinfo.getHandler(config['LOCAL']['IP_INFO_ACCESS_TOKEN'])

    ip_address = req.ip

    if (req.ip == LOCAL_IP_ADDRESS):
        ip_address = '216.239.36.21'

    details = handler.getDetails(ip_address)

    result = create_user(CreateUserArgs(
        req.username,
        req.firstName,
        req.lastName,
        details.city,
        details.country
    ))

    return {
        'token': str(result[0]['_id'])
    }

def check_auth(token:str):
    users = find_user_by_id(token)

    if (len(users) == 0):
        raise Exception("Not authorized")

    return users[0]