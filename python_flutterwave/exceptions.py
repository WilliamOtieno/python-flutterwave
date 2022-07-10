
class TokenException(Exception):
    def __init__(self, token, message):
        self.token = token
        self.message = message

    def __str__(self):
        return f"{self.token} -> {self.message}"


class CustomerDetailException(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class TransactionDetailException(Exception):
    def __init__(self, trans_id, message: str):
        self.message = message
        self.trans_id = trans_id

    def __str__(self):
        return f"{self.trans_id} -> {self.message}"
