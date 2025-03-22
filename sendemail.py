from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_email', methods=['POST'])
def receive_email():
    # Get JSON data sent by Mailjet
    email_data = request.get_json()

    # Extract relevant fields from the incoming email
    sender = email_data.get('Sender')
    recipient = email_data.get('Recipient')
    subject = email_data.get('Subject')
    body = email_data.get('TextPart')

    # For logging purposes, you can print or save the email data
    print(f"Received an email from {sender}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

    # Respond to Mailjet that the email was successfully received
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
