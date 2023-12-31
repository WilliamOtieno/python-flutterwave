### python-flutterwave
- This lib aims to be the middleman between `Flutterwave API` and a python backend. Ergo, it directly makes the API requests to FW and returns the necessary info to the backend.
- One should thoroughly go through the [official docs here](https://developer.flutterwave.com/reference/introduction) in order to have a meaningful insight on how to use the params provided by the functions in the lib.
- The lib will also follow the same project structure as the official docs for ease of use and consistency.

- NB: Set `FW_SECRET_KEY` environnment variable obtained from the dashboard.
  ## Quick Example.

  ```python
  from python_flutterwave.charge import initiate_apple_pay_charge, validate_charge

  details = initiate_apple_pay_charge(tx_ref="your_unique_ref", amount=20, email="johndoe@example.com", currency="USD")
  print(details)
  validation_details = validate_charge(flw_ref="qwerty", otp="123456")
  print(validation_details)
  ```

- More contributors needed, refer to [the contribution gude](/CONTRIBUTING.md)
