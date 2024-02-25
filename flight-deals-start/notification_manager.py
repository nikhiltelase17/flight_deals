from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "ACc16699c2e3ccdf2980f17498ecafa82d"
        self.auth_token = "5410e1c27a7942754c52bc8823ab2ef4"

    def send_message(self, message):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
                body=f"{message}",
                from_='+16592667763',
                to='+918305230871'
            )

        print(message.sid)
