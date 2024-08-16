Here is an example of Python Flask API code that implements the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the notification history in memory for simplicity
notification_history = []

@app.route('/loan/approval', methods=['POST'])
def loan_approval():
    loan_data = request.json

    # Check if the loan status is "Approved"
    if loan_data['status'] == 'Approved':
        # Trigger notification
        send_notification(loan_data)

        # Store the notification in the history
        notification_history.append(loan_data)

        return jsonify({'message': 'Notification sent'})
    else:
        return jsonify({'message': 'Loan not approved'})

def send_notification(loan_data):
    # Get the customer's notification preferences from the database
    customer_preferences = get_notification_preferences(loan_data['customer_id'])

    # Send notification through email
    if customer_preferences['email']:
        send_email_notification(loan_data)

    # Send notification through SMS
    if customer_preferences['sms']:
        send_sms_notification(loan_data)

    # Send notification through in-app notification
    if customer_preferences['in_app']:
        send_in_app_notification(loan_data)

def get_notification_preferences(customer_id):
    # Retrieve the customer's notification preferences from the database
    # Return a dictionary with the preferences (e.g., {'email': True, 'sms': False, 'in_app': True})
    # You can implement this function based on your database structure

    # Example implementation:
    return {'email': True, 'sms': True, 'in_app': True}

def send_email_notification(loan_data):
    # Implement email notification logic here
    pass

def send_sms_notification(loan_data):
    # Implement SMS notification logic here
    pass

def send_in_app_notification(loan_data):
    # Implement in-app notification logic here
    pass

@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notification_history)

if __name__ == '__main__':
    app.run(debug=True)
```

Please note that this is a basic implementation and you will need to fill in the logic for sending notifications through email, SMS, and in-app notifications. You will also need to implement the database functions to retrieve and store notification preferences and history. Additionally, you should consider implementing security measures and compliance with relevant regulations and data protection laws.