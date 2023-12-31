import os
import requests
import json

from python_flutterwave.decorators import handle_api_exceptions


token = os.environ.get("FW_SECRET_KEY")
base_url = "https://api.flutterwave.com/v3/charges"


@handle_api_exceptions
def initiate_bank_charge(
    amount: int,
    email: str,
    tx_ref: str,
) -> dict:
    """
    Collect payments from your customers via bank transfers

    Args:
        tx_ref (int): This is a unique reference peculiar to the transaction being carried out.
        amount (int): This is the amount to be charged for the transaction.
        email (str): The customer's email address.

    Returns: 
        dict: Response Details
    """

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

    return dict(response.json())


@handle_api_exceptions
def initiate_nigeria_bank_charge(
    amount: int,
    email: str,
    tx_ref: str,
) -> dict:
    """
    Charge Nigerian bank accounts using Flutterwave

    Args:
        tx_ref (int): This is a unique reference peculiar to the transaction being carried out.
        amount (int): This is the amount to be charged for the transaction.
        email (str): The customer's email address.

    Returns: 
        dict: Response Details
    """

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

    return dict(response.json())


@handle_api_exceptions
def initiate_uk_eu_bank_charge(
    amount: int, email: str, tx_ref: str, phone_number: str, is_token_io: int
) -> dict:
    """
    Charge Customers UK and EU bank accounts

    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        amount (int): Amount to be charged for the transaction.
        email (str): The customer's email address.
        phone_number (str): Phone number linked to the customer's bank account or mobile money account
        is_token_io (int):

    Returns: 
        dict: Response Details
    """

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

    return dict(response.json())


@handle_api_exceptions
def initiate_ach_bank_charge(
    amount: int,
    email: str,
    tx_ref: str,
    phone_number: str,
    currency: str,
) -> dict:
    """
    Collect ACH payments for USD and ZAR transactions

    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        amount (int): Amount to be charged for the transaction.
        email (str): The customer's email address.
        phone_number (str): Phone number linked to the customer's bank account or mobile money account
        currency (str): Currency to charge in. Expected values are ZAR for ZA ACH and USD for US ACH.

    Returns: 
        dict: Response Details
    """

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

    return dict(response.json())
