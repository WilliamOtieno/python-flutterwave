import os
import requests
import json

from python_flutterwave.decorators import handle_api_exceptions


token = os.environ.get("SECRET_KEY")
base_url = "https://api.flutterwave.com/v3/charges"


@handle_api_exceptions
def initiate_mpesa_charge(
    amount: int, email: str, tx_ref: str, phone_number: str
) -> dict:
    """
    Collect Mpesa payments from customers in Kenya
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :return: dict
    """

    params = {"type": "mpesa"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
            "currency": "KES",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_ghana_mobile_charge(
    amount: int, email: str, tx_ref: str, phone_number: str, network: str
) -> dict:
    """
    Collect mobile money payments from customers in Ghana
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :param network: str
    :return: dict
    """

    params = {"type": "mobile_money_ghana"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
            "network": f"{network}",
            "currency": "GHS",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_uganda_mobile_charge(
    amount: int,
    email: str,
    tx_ref: str,
    phone_number: str,
) -> dict:
    """
    Collect mobile money payments from customers in Uganda
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :return: dict
    """

    params = {"type": "mobile_money_uganda"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
            "currency": "UGX",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_franco_mobile_charge(
    amount: int,
    email: str,
    tx_ref: str,
    phone_number: str,
    currency: str,
    franco_country_code: str,
) -> dict:
    """
    Collect mobile money payments from customers in Francophone countries
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :param currency: str,
    :param franco_country_code: str
    :return: dict
    """

    params = {"type": "mobile_money_franco"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
            "currency": f"{currency}",
            "country": franco_country_code,
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_tanzania_mobile_charge(
    amount: int,
    email: str,
    tx_ref: str,
    phone_number: str,
) -> dict:
    """
    Collect mobile money payments from customers in Tanzania
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :return: dict
    """

    params = {"type": "mobile_money_tanzania"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
            "currency": "TZS",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_rwanda_mobile_charge(
    amount: int, email: str, tx_ref: str, phone_number: str, order_id: str
) -> dict:
    """
    Collect mobile money payments from customers in Rwanda
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :param order_id: str
    :return: dict
    """

    params = {"type": "mobile_money_rwanda"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
            "order_id": f"{order_id}",
            "currency": "RWF",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_zambia_mobile_charge(
    amount: int,
    email: str,
    tx_ref: str,
    phone_number: str,
) -> dict:
    """
    Collect mobile money payments from customers in Zambia
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :return: dict
    """

    params = {"type": "mobile_money_zambia"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
            "currency": "ZMW",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_ussd_charge(
    tx_ref: str,
    account_bank: str,
    amount: int,
    email: str,
    phone_number: str,
) -> dict:
    """
    Collect USSD payments from customers in Nigeria
    :param tx_ref: str
    :param account_bank: str
    :param amount: int
    :param email: str
    :param phone_number: str
    :return: dict
    """

    params = {"type": "ussd"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "account_bank": f"{account_bank}",
            "amount": f"{amount}",
            "currency": "NGN",
            "email": f"{email}",
            "phone_number": f"{phone_number}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_apple_pay_charge(
    tx_ref: str,
    amount: int,
    email: str,
    currency: str,
) -> dict:
    """
    Accept payments from your customers with Apple Pay
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param currency: str
    :return: dict
    """

    params = {"type": "applepay"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "currency": f"{currency}",
            "email": f"{email}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_google_pay_charge(
    tx_ref: str,
    amount: int,
    email: str,
    currency: str,
) -> dict:
    """
    Accept payments from your customers with Google Pay
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param currency: str
    :return: dict
    """

    params = {"type": "googlepay"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "currency": f"{currency}",
            "email": f"{email}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_enaira_charge(
    tx_ref: str,
    amount: int,
    email: str,
) -> dict:
    """
    Accept payment from eNaira wallets
    :param tx_ref: str
    :param amount: int
    :param email: str
    :return: dict
    """

    params = {"type": "enaira"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "email": f"{email}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_fawry_pay_charge(
    tx_ref: str,
    amount: int,
    email: str,
) -> dict:
    """
    Receive Fawry payments from customers in Egypt
    :param tx_ref: str
    :param amount: int
    :param email: str
    :return: dict
    """

    params = {"type": "fawry_pay"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "currency": "EGP",
            "email": f"{email}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(base_url, headers=headers, data=payload, params=params)

    return dict(response.json())


@handle_api_exceptions
def initiate_paypal_charge(
    tx_ref: str,
    amount: int,
    email: str,
    currency: str,
) -> dict:
    """
    Collect payments from customers with PayPal
    :param tx_ref: str
    :param amount: int
    :param email: str
    :param currency: str
    :return: dict
    """

    params = {"type": "paypal"}
    payload = json.dumps(
        {
            "tx_ref": f"{tx_ref}",
            "amount": f"{amount}",
            "currency": f"{currency}",
            "email": f"{email}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(base_url, headers=headers, data=payload, params=params)

    return dict(response.json())
