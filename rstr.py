# random string generator use for auth codes
import base64
import secrets
import flask


def create_string():
    key1: str = secrets.token_hex()
    key2: str = secrets.token_hex()
    key3 = base64.b64encode(bytes(key1.join(key2).encode("ascii")))
    return key3

def check_string(keyin_a: str, keyin_b:str) -> bool:
    keys_a = base64.b64decode(keyin_a)
    keys_b = base64.b64decode(keyin_b)
    key_a1 = keys_a[:64]
    key_a2 = keys_a[65:]
    key_b1 = keys_b[:64]
    key_b2 = keys_b[65:]
    if not 

def getSessionArgs(login: bool):
    if login:
        newCode: str = create_string()
        flask.session['authCode'] = newCode
        flask.session.new = False
        flask.session.modified = True
    authCode: str = flask.session['authCode']
    return authCode

if __name__ == "__main__":
    print(create_string())