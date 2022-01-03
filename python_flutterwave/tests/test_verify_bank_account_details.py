import os
import unittest
from python_flutterwave import payment


class TestVerifyBankAccountDetails(unittest.TestCase):
    def setUp(self) -> None:
        self.token = os.environ.get("SECRET_KEY")
        self.account_number = "0690000032"
        self.account_bank = "044"

        payment.token = self.token
        self.details = payment.verify_bank_account_details(account_bank=self.account_bank,
                                                           account_number=self.account_number)

    def tearDown(self) -> None:
        pass

    def test_argument_types(self):
        self.assertIsInstance(self.token, str)
        self.assertIsInstance(self.account_number, str)
        self.assertIsInstance(self.account_bank, str)

    def test_mandatory_args(self):
        self.assertIsNot(self.token, "")
        self.assertIsNot(self.account_bank, "")
        self.assertIsNot(self.account_number, "")

    def test_return_obj(self):
        self.assertIsInstance(self.details, dict)
        self.assertIsNotNone(self.details)
        self.assertIn("status", self.details.keys())
        self.assertIn("message", self.details.keys())
        self.assertIn("data", self.details.keys())
        self.assertNotEqual(self.details["status"], "error")
        self.assertNotEqual(self.details["data"], "null")
