import os
import requests
import json
from python_flutterwave.decorators import handle_api_exceptions

token = os.environ.get("FW_SECRET_KEY")


@handle_api_exceptions
def validate_charge(otp: str, flw_ref: str) -> dict:
    """
    Validate a charge
    
    Args:
        flw_ref (str): Reference returned in the initiate charge call as `data.flw_ref`
        otp (str): Random number of at least 6 characters sent to customers phone number.

    Returns: 
        dict: Response Details
    """

    params = {"type": "mpesa"}
    payload = json.dumps(
        {
            "flw_ref": f"{flw_ref}",
            "otp": f"{otp}",
        }
    )
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    base_url = "https://api.flutterwave.com/v3/validate-charge"
    response = requests.post(url=base_url, headers=headers, data=payload, params=params)

    return dict(response.json())
