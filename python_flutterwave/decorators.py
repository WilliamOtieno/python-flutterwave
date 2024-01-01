import os
import requests
from functools import wraps
from .exceptions import TokenException, FlutterwaveAPIException


token = os.environ.get("FW_SECRET_KEY")


def require_token(func):
    """Ascertain existence of the auth token"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if token == "" or token is None:
            raise TokenException(token=token, message="Authentication token absent")
        return func(*args, **kwargs)

    return wrapper


def handle_api_exceptions(func):
    """Raise exceptions whenever necessary"""
    @wraps(func)
    @require_token
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            raise FlutterwaveAPIException(f"Request Exception: {str(e)}")
        except Exception as ex:
            raise FlutterwaveAPIException(str(ex))

    return wrapper
