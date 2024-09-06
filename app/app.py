```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cases.db'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
mail = Mail(app)

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remarks = db.Column(db.String(200))
    status = db.Column(db.String(50))
    qc2_remarks = db.Column(db.String(200))

@app.route('/ff_approval_request', methods=['POST'])
def ff_approval_request():
    data = request.json
    new_case = Case(remarks=data['remarks'], status='F&F Approval Pending with QC2')
    db.session.add(new_case)
    db.session.commit()
    
    msg = Message('F&F Approval Request', sender='your-email@example.com', recipients=['qc2@example.com'])
    msg.body = f"New F&F approval request with remarks: {data['remarks']}"
    mail.send(msg)
    
    return jsonify({'message': 'Request submitted successfully'}), 201

@app.route('/review_request/<int:case_id>', methods=['POST'])
def review_request(case_id):
    data = request.json
    case = Case.query.get(case_id)
    if not case:
        return jsonify({'message': 'Case not found'}), 404
    
    case.qc2_remarks = data['qc2_remarks']
    case.status = 'Approved' if data['approved'] else 'Rejected'
    db.session.commit()
    
    return jsonify({'message': 'Review submitted successfully'}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```