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
   	
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        amount (int): Amount to be charged for the transaction.
        email (str): The customer's email address.
        currency (str): Currency to be used
        token (str): Card token returned from the transaction verification endpoint as data.card.token

    Returns: 
        dict: Response Details
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

    Args:
        retry_strategy: RetryStrategy
        bulk_data: list[ChargeData]
    
    Returns:
        dict: Response Details
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
   	
    Args:
        bulk_id (int): id returned in the bulk charge response

    Returns:
        dict: Response Details
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

    Args:
        bulk_id (int): id returned in the bulk charge response

    Returns:
        dict: Response Details
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
   	
    Args:
        email (str): The customer's email address.
        full_name (str): The customer's email address.
        phone_number (str): Customer's phone number.
        token (str): Card token returned from the transaction verification endpoint as data.card.token

    Returns: 
        dict: Response Details
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
