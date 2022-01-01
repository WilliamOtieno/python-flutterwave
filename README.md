# Python Flutterwave

### Description
Python Wrapper for interacting with the Flutterwave API


## Installation

- ``pip install python-flutterwave``

## Usage

- Create an account in Flutterwave and obtain your `Secret Key` only.

```
from python_flutterwave import payment

payment.token = 'YOUR_SECRET_KEY'
```

- To trigger a standard payment that returns a redirect uri

```
uri = payment.initiate_payment(tx_ref="qwerty", amount=100, redirect_url='your_callback_url',
                               payment_options='mpesa', customer_email='example@email.com',
                               customer_phone_number='0123456789', currency='KES', customer_name='John Doe',
                               title='Demo Payment', description='Just pay me...')
print(uri)
```
- Redirect the user to that uri where he/she will make the payment. 
- After payment is made, the user will be redirected to the `redirect_url` you declared but Flutterwave will append some
info regarding the payment i.e. `transaction_id` and `tx_ref`. If your url is `https://example.com/callback`
then it may be `http://example.com/callback/?status=successful&tx_ref=qwerty&transaction_id=2784792`
- You should save the transaction_id to your DB as it will be used to query the transaction details.


- To check the transaction details e.g. successful or not, grab the transaction_id from the previous step. 
```
details = payment.get_payment_details(transaction_id)
print(details)
```

- To trigger an automatic MPESA charge on your customer through STK push, first configure your Webhook url in the dashboard, it may be a
simple server; Flutterwave will post some data regarding your transaction status in that url. This method call will
return a Python dict object. You can decide what to do thereon.
```
mpesa_trans_details = payment.trigger_mpesa_payment(tx_ref="qwertyuio", amount=100, currency='KES', 
                                                    email='johndoe@gmail.com', phone_number='1234567890', 
                                                    full_name='John Doe')
print(mpesa_trans_details)
```

- To initiate a USSD payment to your customer, configure your webhook url in the dashboard where Flutterwave will post data
regarding the transaction. This method call will return a Python Dict object from which you can extract the USSD code to 
show your customer for payment completion. For other banks, you may also need to extract the `payment_code` from the result.
  
  - By default, `NGN` is the only supported currency for USSD payments so this method automatically uses `NGN`
  - Only a number of banks support `USSD` so you have to refer to the docs to check your bank and its corresponding `account_bank` code.
```
details = payment.initiate_ussd_payment(tx_ref="123erd", amount=100, email='johndoe@gmail.com',
                                        phone_number='789456123', full_name='John Doe', account_bank='057')
print(details)
```
