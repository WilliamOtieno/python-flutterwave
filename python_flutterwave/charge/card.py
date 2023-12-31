import os
import requests
import json

from python_flutterwave.decorators import handle_api_exceptions


token = os.environ.get("SECRET_KEY")
base_url = "https://api.flutterwave.com/v3/charges"


@handle_api_exceptions
def initiate_card_charge(
    amount: int,
    card_number: int,
    cvv: int,
    expiry_month: int,
    expiry_year: int,
    email: str,
    tx_ref: str,
) -> dict:
    """
    This is used to initiate card payments.
    :param tx_ref: str
    :param amount: int
    :param card_number: int
    :param cvv: int
    :param expiry_month: int
    :param expiry_year: int
    :param email: str
    :return: dict
    """

    params = {"type": "card"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "card_number": f"{card_number}",
            "cvv": f"{cvv}",
            "expirty_month": f"{expiry_month}",
            "expirty_year": f"{expiry_year}",
            "email": f"{email}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())
