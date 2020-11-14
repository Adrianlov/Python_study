from twilio.rest import Client

account_sid = 'ACe26695c8cb5d69aa09807c25c5701afe'
auth_token = '8f199b0e0d9d788199096757c6f7e26f'
client = Client(account_sid, auth_token)
def send_love():

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Te iubesc si ma gandesc la tine, te sarut suflet dulce',
    to='whatsapp:+40729228835'
)

    print(message.sid)