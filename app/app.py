Sure! Here's an example of a Python Flask API code that implements the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/apply', methods=['POST'])
def apply_for_loan():
    # Get the loan application details from the request
    application_details = request.get_json()

    # Validate the entered details
    if not validate_details(application_details):
        return jsonify({'error': 'Invalid details'}), 400

    # Store the application details securely
    store_application_details(application_details)

    # Send a confirmation message to the customer
    send_confirmation_message(application_details['email'])

    return jsonify({'message': 'Loan application submitted successfully'})

def validate_details(details):
    # Perform validation logic here
    # Return True if details are valid, False otherwise
    return True

def store_application_details(details):
    # Store the application details securely
    # Implement the storage logic here
    pass

def send_confirmation_message(email):
    # Send a confirmation message to the customer
    # Implement the message sending logic here
    pass

if __name__ == '__main__':
    app.run()
```

In this code, we define a Flask API with a single route `/apply` that accepts POST requests. The `apply_for_loan` function handles the loan application process. It validates the entered details, stores the application details securely, and sends a confirmation message to the customer.

Please note that this is a basic example and you may need to modify it to fit your specific requirements and integrate it with your database and email sending services.