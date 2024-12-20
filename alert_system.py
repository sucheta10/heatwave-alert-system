from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

def send_alert(message, phone_number):
    """Send an alert to a user."""
    client.messages.create(
        body=message,
        from_='+1234567890',  # Replace with your Twilio phone number
        to=phone_number
    )
