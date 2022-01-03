import os
import unittest
import random
import string

from python_flutterwave import payment


class TestInitiateUSSDPayment(unittest.TestCase):

    def setUp(self) -> None:
        self.token = os.environ.get("SECRET_KEY")
        self.tx_ref = f"{''.join(random.choice(string.ascii_letters) for i in range(10))}"
        self.amount = 10.0
        self.account_bank = "044"
        self.email = "johndoe@gmail.com"
        self.phone_number = "1234567890"
        self.full_name = "John Doe"
        payment.token = self.token
        self.details = payment.initiate_ussd_payment(tx_ref=self.tx_ref, amount=self.amount,
                                                     email=self.email, phone_number=self.phone_number,
                                                     full_name=self.full_name, account_bank=self.account_bank)

    def tearDown(self) -> None:
        pass

    def test_argument_types(self):
        self.assertIsInstance(self.token, str)
        self.assertIsInstance(self.tx_ref, str)
        self.assertIsInstance(self.amount, float)
        self.assertIsInstance(self.account_bank, str)

    def test_mandatory_args(self):
        self.assertIsNot(self.token, "")
        self.assertIsNot(self.amount, "")
        self.assertIsNot(self.email, "")
        self.assertIsNot(self.account_bank, "")
        self.assertIsNot(self.phone_number, "")

    def test_return_obj(self):
        self.assertIsInstance(self.details, dict)
        self.assertIsNotNone(self.details)
        self.assertIn("status", self.details.keys())
        self.assertIn("message", self.details.keys())
        self.assertIn("data", self.details.keys())
        self.assertIn("meta", self.details.keys())
