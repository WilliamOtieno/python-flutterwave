from dataclasses import dataclass


@dataclass
class RetryStrategy:
    """
    This object defines retries for failed tokenization attempts.

    Args:
        retry_interval (int): Number in minutes for the next retry attempt.
        retry_amount_variable (int): Amount to be retried after the specified number of attempts in percentage.
        retry_attempt_variable (int): Number of retries to make after the initial tokenization attempt.
        last_retry_attempt (int): Maximum number of retries to attempt. If unspecified, It is set to 10 by default.
    """

    retry_interval: int
    retry_amount_variable: int
    retry_attempt_variable: int
    last_retry_attempt: int = 10


@dataclass
class ChargeData:
    """
    Object containing your charge data

    Args:
        currency (str): Currency to charge in
        token (str): Token id obtained 
        country (str): Country Code
        amount (int): Charge Amount
        email (str): Customer Email
        tx_ref (str): Unique ref
    """

    currency: str
    token: str
    country: str
    amount: int
    email: str
    tx_ref: str
