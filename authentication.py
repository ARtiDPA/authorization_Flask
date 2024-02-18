from jwt import encode, decode


secret_key = "qazwsxedc_QAZWSXEDC"


def create_token(id):
    payload = {"user_id": id}
    token = encode(payload, secret_key, algorithm="HS256")
    return token


def decoding(token):
    verified_token = decode(token, secret_key, algorithms='HS256')
    return verified_token


def check(token):
    decod_token = decoding(token)
    id = decod_token.get("user_id")
    print(id)
    return id
