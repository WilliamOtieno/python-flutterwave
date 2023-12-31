from dataclasses import dataclass


@dataclass
class RetryStrategy:
    """
    This object defines retries for failed tokenization attempts.
    :param retry_interval: int
    :param retry_amount_variable: int
    :param retry_attempt_variable: int
    :param last_retry_attempt: int = 10
    """

    retry_interval: int
    retry_amount_variable: int
    retry_attempt_variable: int
    last_retry_attempt: int = 10


@dataclass
class ChargeData:
    """
    Object containing your charge data
    :param currency: str
    :param token: str
    :param country: str
    :param amount: int
    :param email: str
    :param tx_ref: str
    """

    currency: str
    token: str
    country: str
    amount: int
    email: str
    tx_ref: str
