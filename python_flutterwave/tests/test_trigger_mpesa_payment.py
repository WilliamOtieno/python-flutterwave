import random
import string
import unittest
import os

from python_flutterwave import payment


class TestTriggerMpesaPayment(unittest.TestCase):

    def setUp(self) -> None:
        self.token = os.environ.get("SECRET_KEY")
        self.tx_ref = f"{''.join(random.choice(string.ascii_letters) for i in range(10))}"
        self.amount = 10.0
        self.currency = 'KES'
        self.email = "johndoe@gmail.com"
        self.phone_number = "1234567890"
        self.full_name = "John Doe"
        payment.token = self.token
        self.details = payment.trigger_mpesa_payment(tx_ref=self.tx_ref, amount=self.amount, currency=self.currency,
                                                     email=self.email, phone_number=self.phone_number,
                                                     full_name=self.full_name)

    def tearDown(self) -> None:
        pass

    def test_argument_types(self):
        self.assertIsInstance(self.token, str)
        self.assertIsInstance(self.tx_ref, str)
        self.assertIsInstance(self.amount, float)
        self.assertIsInstance(self.currency, str)

    def test_mandatory_args(self):
        self.assertIsNot(self.token, "")
        self.assertIsNot(self.amount, "")
        self.assertIsNot(self.email, "")

    def test_return_obj(self):
        self.assertIsInstance(self.details, dict)
        self.assertIsNotNone(self.details)
        self.assertIn("status", self.details.keys())
        self.assertIn("message", self.details.keys())
        self.assertIn("data", self.details.keys())
