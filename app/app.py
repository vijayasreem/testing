Sure! Here's an example of a Python Flask API code that filters a list of customer data by age:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/filter_customers', methods=['POST'])
def filter_customers():
    customers = request.json.get('customers', [])
    age_range = request.json.get('age_range', '')

    filtered_customers = []
    if customers and age_range:
        min_age, max_age = map(int, age_range.split('-'))
        filtered_customers = [customer for customer in customers if min_age <= customer['age'] <= max_age]

    return jsonify(filtered_customers)

if __name__ == '__main__':
    app.run(debug=True)
```

To test the API, you can send a POST request to `http://localhost:5000/filter_customers` with the following JSON payload:

```json
{
  "customers": [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 40}
  ],
  "age_range": "20-30"
}
```

The API will return the filtered list of customers within the specified age range:

```json
[
  {"name": "John", "age": 30},
  {"name": "Alice", "age": 25}
]
```

If the `customers` list is empty or the `age_range` is not specified, the API will return an empty list.

Please note that this is a basic implementation and you may need to modify it based on your specific requirements.