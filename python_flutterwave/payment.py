import requests
import json
from typing import Optional

token = ""


def initiate_payment(tx_ref: str, amount: float, currency: str, redirect_url: str, payment_options: str,
                     customer_email: str, customer_phone_number: Optional[str], customer_name: str,
                     title: Optional[str],
                     description: Optional[str]) -> str:
    """This is used to initiate payments. It takes in the arguments and returns the url to redirect users for
    payments """
    payment_url = "https://api.flutterwave.com/v3/payments"
    payload = json.dumps({
        "tx_ref": f"{tx_ref}",
        "amount": f"{amount}",
        "currency": f"{currency}",
        "redirect_url": f"{redirect_url}",
        "payment_options": f"{payment_options}",
        "customer": {
            "email": f"{customer_email}",
            "phonenumber": f"{customer_phone_number}",
            "name": f"{customer_name}"
        },
        "customizations": {
            "title": f"{title}",
            "description": f"{description}",
        }
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.request(method="POST", url=payment_url, headers=headers, data=payload)
    link = response.json()["data"]["link"]
    return link


def get_payment_details(trans_id: str):
    """
    Takes the transaction_id from the request and returns the status info in json.
    It transaction_id is different from the transaction_ref so it should be grabbed from the request in the redirect url

    """
    url = f"https://api.flutterwave.com/v3/transactions/{trans_id}/verify"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
