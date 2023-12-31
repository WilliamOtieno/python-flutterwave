class FlutterwaveAPIException(Exception):
    pass


class TokenException(FlutterwaveAPIException):
    def __init__(self, token, message):
        super().__init__(f"Token Error: {message}")
        self.token = token
