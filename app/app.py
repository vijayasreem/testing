Sure! Here's an example of a Python Flask API code that can help optimize traffic load for swift response and effective incident management:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incident.db'
db = SQLAlchemy(app)

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Open')

    def __repr__(self):
        return f"Incident('{self.title}', '{self.status}')"

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    result = []
    for incident in incidents:
        result.append({
            'id': incident.id,
            'title': incident.title,
            'description': incident.description,
            'status': incident.status
        })
    return jsonify(result)

@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    incident = Incident(title=data['title'], description=data['description'])
    db.session.add(incident)
    db.session.commit()
    return jsonify({'message': 'Incident created successfully'})

if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a Flask API with two endpoints: `/incidents` for retrieving incidents and `/incidents` (POST) for creating incidents. It uses SQLite as the database for storing incidents.

To optimize traffic load and ensure swift response, you can consider the following strategies:

1. Use a load balancer to distribute incoming requests across multiple servers.
2. Implement caching mechanisms to reduce the load on the database.
3. Use asynchronous processing for time-consuming tasks to avoid blocking the main thread.
4. Implement rate limiting to prevent abuse and ensure fair resource allocation.
5. Monitor system performance and use performance profiling tools to identify bottlenecks and optimize code.

Remember to customize and enhance this code based on your specific requirements and infrastructure setup.