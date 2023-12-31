import os
import requests
import json
from dataclasses import asdict
from python_flutterwave.decorators import handle_api_exceptions
from python_flutterwave.objects import ChargeData, RetryStrategy

auth_token = os.environ.get("FW_SECRET_KEY")


@handle_api_exceptions
def initiate_tokenized_charge(
    amount: int, email: str, tx_ref: str, currency: str, token: str
) -> dict:
    """
    This endpoint helps you tokenize a customer's card
    :param token: str
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param currency: str
    :return: dict
    """

    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "token": f"{token}",
            "currency": f"{currency}",
        }
    )
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        url="https://api.flutterwave.com/v3/tokenized-charges",
        headers=headers,
        data=payload,
    )

    return dict(response.json())


@handle_api_exceptions
def initiate_bulk_tokenized_charges(
    retry_strategy: RetryStrategy, bulk_data: list[ChargeData]
) -> dict:
    """
    Tokenize multiple cards at once
    :param retry_strategy: RetryStrategy
    :param bulk_data: list[ChargeData]
    :return: dict
    """

    payload = json.dumps(
        {
            "retry_strategy": asdict(retry_strategy),
            "bulk_data": [asdict(i) for i in bulk_data],
        }
    )
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        url="https://api.flutterwave.com/v3/bulk-tokenized-charges",
        headers=headers,
        data=payload,
    )

    return dict(response.json())


@handle_api_exceptions
def fetch_bulk_tokenized_charges(bulk_id: int):
    """
    This endpoint allows you to get bulk tokenized charges transactions
    :param bulk_id: int
    """

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    response = requests.get(
        url=f"https://api.flutterwave.com/v3/bulk-tokenized-charges/{bulk_id}/transactions",
        headers=headers,
    )

    return dict(response.json())


@handle_api_exceptions
def fetch_bulk_tokenized_charges_status(bulk_id: int):
    """
    This endpoint allows you to query the status of a bulk tokenized charge
    :param bulk_id: int
    """

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    response = requests.get(
        url=f"https://api.flutterwave.com/v3/bulk-tokenized-charges/{bulk_id}",
        headers=headers,
    )

    return dict(response.json())


@handle_api_exceptions
def update_card_token(email: str, full_name: str, phone_number: str, token: str):
    """
    This endpoints allow developers update the details tied to a customer's card token.
    :param email: str
    :param phone_number: str
    :param full_name: str
    :param token: str
    """

    payload = json.dumps(
        {
            "email": f"{email}",
            "full_name": f"{full_name}",
            "phone_number": f"{phone_number}",
        }
    )

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    response = requests.get(
        url=f"https://api.flutterwave.com/v3/tokens/{token}",
        headers=headers,
        data=payload,
    )

    return dict(response.json())
