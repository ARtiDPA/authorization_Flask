from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity


def generate_assecc_token(user_id):
    access_token = create_access_token(identity=user_id)
    return access_token


def generate_refresh_token(user_id):
    refresh_token = create_refresh_token(identity=user_id)
    return refresh_token
