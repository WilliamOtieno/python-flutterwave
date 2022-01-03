import random
import string
import unittest
import os

from python_flutterwave import payment


class TestStandardPayment(unittest.TestCase):

    def setUp(self) -> None:
        self.token = os.environ.get("SECRET_KEY")
        self.tx_ref = f"{''.join(random.choice(string.ascii_letters) for i in range(10))}"
        self.amount = 10.0
        self.currency = 'KES'
        self.redirect_url = "https://example.com/"
        self.payment_options = "mpesa"
        self.customer_email = "johndoe@gmail.com"
        self.customer_phone_number = "1234567890"
        self.customer_name = "John Doe"
        self.title = "Test Payment"
        self.description = "Just pay me..."
        payment.token = self.token
        self.link = payment.initiate_payment(tx_ref=self.tx_ref, amount=self.amount, redirect_url=self.redirect_url,
                                             payment_options=self.payment_options, customer_email=self.customer_email,
                                             customer_phone_number=self.customer_phone_number,
                                             customer_name=self.customer_name, title=self.title,
                                             description=self.description, currency=self.currency)

    def tearDown(self) -> None:
        pass

    def test_argument_types(self):
        self.assertIsInstance(self.token, str)
        self.assertIsInstance(self.tx_ref, str)
        self.assertIsInstance(self.amount, float)
        self.assertIsInstance(self.currency, str)
        self.assertIsInstance(self.redirect_url, str)
        self.assertIsInstance(self.payment_options, str)
        self.assertIsInstance(self.customer_email, str)
        self.assertIsInstance(self.customer_phone_number, str)
        self.assertIsInstance(self.customer_name, str)
        self.assertIsInstance(self.title, str)
        self.assertIsInstance(self.description, str)

    def test_mandatory_args(self):
        self.assertIsNot(self.token, "")
        self.assertIsNot(self.amount, "")
        self.assertIsNot(self.customer_email, "")

    def test_return_obj(self):
        self.assertIsInstance(self.link, str)
        self.assertIsNotNone(self.link)
