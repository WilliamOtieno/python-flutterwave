import os
import requests
import json

from python_flutterwave.decorators import handle_api_exceptions


token = os.environ.get("FW_SECRET_KEY")
base_url = "https://api.flutterwave.com/v3/charges"


@handle_api_exceptions
def initiate_mpesa_charge(
    amount: int, email: str, tx_ref: str, phone_number: str
) -> dict:
    """
    Collect Mpesa payments from customers in Kenya
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        phone_number (str): Phone number linked to the customer's bank account or mobile money account

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        phone_number (str): Phone number linked to the customer's bank account or mobile money account
        
        network (str): Mobile money network provider (MTN, VODAFONE, TIGO)

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        phone_number (str): Phone number linked to the customer's bank account or mobile money account

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        phone_number (str): Phone number linked to the customer's bank account or mobile money account
        
        currency (str): Currency to charge in. 
        
        franco_country_code (str): Country code (BF, CI, CM, SN)

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        phone_number (str): Phone number linked to the customer's bank account or mobile money account

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        phone_number (str): Phone number linked to the customer's bank account or mobile money account
        
        order_id (str): Unique ref for the mobilemoney transaction to be provided by the merchant

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        phone_number (str): Phone number linked to the customer's bank account or mobile money account

    Returns: 
        dict: Response Details
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

    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        account_bank (str): Bank numeric code. It can be gotten from the banks endpoint.
        
        phone_number (str): Phone number linked to the customer's bank account or mobile money account

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        currency (str): Currency to charge in. 

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        currency (str): Currency to charge in. 

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): This is a unique reference peculiar to the transaction being carried out.
        
        amount (int): This is the amount to be charged for the transaction.
        
        email (str): The customer's email address.

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): This is a unique reference peculiar to the transaction being carried out.
        
        amount (int): This is the amount to be charged for the transaction.
        
        email (str): The customer's email address.

    Returns: 
        dict: Response Details
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
    
    Args:
        tx_ref (int): Unique reference peculiar to the transaction.
        
        amount (int): Amount to be charged for the transaction.
        
        email (str): The customer's email address.
        
        currency (str): Currency to charge in.
    
    Returns: 
        dict: Response Details
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
