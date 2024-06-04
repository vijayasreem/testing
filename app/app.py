Sure! Here's an example of a Python Flask API code that can be used to implement the given user story:

```python
from flask import Flask, request

app = Flask(__name__)

# API endpoint for loan application submission
@app.route('/loan-application', methods=['POST'])
def submit_loan_application():
    # Process loan application logic here
    return 'Loan application submitted successfully'

# API endpoint for regulatory requirement changes
@app.route('/regulatory-changes', methods=['POST'])
def handle_regulatory_changes():
    # Process regulatory changes logic here
    return 'Regulatory changes handled successfully'

# API endpoint for business process changes
@app.route('/business-process-changes', methods=['POST'])
def handle_business_process_changes():
    # Process business process changes logic here
    return 'Business process changes handled successfully'

if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a Flask application with three API endpoints: `/loan-application`, `/regulatory-changes`, and `/business-process-changes`. Each endpoint is associated with a specific functionality mentioned in the user story.

You can add the necessary logic inside each endpoint to handle loan application submissions, regulatory changes, and business process changes. Additionally, you can implement the mechanisms for scalability, adaptability, version control, and documentation as per the acceptance criteria.

Note: This is a basic example to get you started. You may need to modify and expand the code based on your specific requirements and implementation details.