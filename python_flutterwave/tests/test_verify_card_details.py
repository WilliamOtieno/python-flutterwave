import os
import unittest
from python_flutterwave import payment


class TestVerifyCardDetails(unittest.TestCase):
    def setUp(self) -> None:
        self.token = os.environ.get("SECRET_KEY")
        self.card_bin = "553188"

        payment.token = self.token
        self.details = payment.verify_card_details(card_bin=self.card_bin)

    def tearDown(self) -> None:
        pass

    def test_argument_types(self):
        self.assertIsInstance(self.token, str)
        self.assertIsInstance(self.card_bin, str)

    def test_mandatory_args(self):
        self.assertIsNot(self.token, "")
        self.assertIsNot(self.card_bin, "")

    def test_return_obj(self):
        self.assertIsInstance(self.details, dict)
        self.assertIsNotNone(self.details)
        self.assertIn("status", self.details.keys())
        self.assertIn("message", self.details.keys())
        self.assertIn("data", self.details.keys())
        self.assertNotEqual(self.details["status"], "error")
        self.assertNotEqual(self.details["data"], "null")
