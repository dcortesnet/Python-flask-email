from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '<your-email>@gmail.com'
app.config['MAIL_PASSWORD'] = '<your-app-password>'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ('<your name sender>', '<your-email>@gmail.com')

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    json = request.get_json()
    subject = json.get('subject')
    recipients = json.get('recipients')
    body = json.get('body')

    if not subject or not recipients or not body:
        return jsonify({"message": "The fields subject, recipient and body is required"}), 400

    try:
        msg = Message(
            subject=subject,
            recipients=recipients,
            body=body
        )
        mail.send(msg)
        return jsonify({"message": 'Email sent successful!'}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')