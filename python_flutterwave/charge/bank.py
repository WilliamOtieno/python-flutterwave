import os
import requests
import json

from python_flutterwave.exceptions import TokenException


token = os.environ.get("SECRET_KEY")
base_url = "https://api.flutterwave.com/v3/charges"


def initiate_bank_charge(
    amount: int,
    email: str,
    tx_ref: str,
) -> dict:
    """
    Collect payments from your customers via bank transfers
    :param tx_ref: str
    :param amount: int
    :param email: str
    :return: dict
    """

    if token == "" or token is None:
        raise TokenException(token=token, message="Authentication token absent")

    params = {"type": "bank_transfer"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)
    if response.status_code == 401:
        raise TokenException(token=token, message="Invalid token provided")
    if response.status_code == 400:
        raise Exception(f"{response.json()['message']}")
    if response.status_code >= 400:
        raise Exception(response.text)

    return dict(response.json())


def initiate_nigeria_bank_charge(
    amount: int,
    email: str,
    tx_ref: str,
) -> dict:
    """
    Charge Nigerian bank accounts using Flutterwave
    :param tx_ref: str
    :param amount: int
    :param email: str
    :return: dict
    """

    if token == "" or token is None:
        raise TokenException(token=token, message="Authentication token absent")

    params = {"type": "mono"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)
    if response.status_code == 401:
        raise TokenException(token=token, message="Invalid token provided")
    if response.status_code == 400:
        raise Exception(f"{response.json()['message']}")
    if response.status_code >= 400:
        raise Exception(response.text)

    return dict(response.json())


def initiate_uk_eu_bank_charge(
    amount: int, email: str, tx_ref: str, phone_number: str, is_token_io: int
) -> dict:
    """
    Charge Customers UK and EU bank accounts
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :param is_token_io: int
    :return: dict
    """

    if token == "" or token is None:
        raise TokenException(token=token, message="Authentication token absent")

    params = {"type": "account-ach-uk"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
            "is_token_io": is_token_io,
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)
    if response.status_code == 401:
        raise TokenException(token=token, message="Invalid token provided")
    if response.status_code == 400:
        raise Exception(f"{response.json()['message']}")
    if response.status_code >= 400:
        raise Exception(response.text)

    return dict(response.json())


def initiate_ach_charge(
    amount: int,
    email: str,
    tx_ref: str,
    phone_number: str,
    currency: str,
) -> dict:
    """
    Collect ACH payments for USD and ZAR transactions
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :param currency: str
    :return: dict
    """

    if token == "" or token is None:
        raise TokenException(token=token, message="Authentication token absent")

    params = {"type": "account-ach-uk"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "currency": f"{currency}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)
    if response.status_code == 401:
        raise TokenException(token=token, message="Invalid token provided")
    if response.status_code == 400:
        raise Exception(f"{response.json()['message']}")
    if response.status_code >= 400:
        raise Exception(response.text)

    return dict(response.json())
