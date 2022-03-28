from django.db import models

from twilio.rest import Client
# Create your models here.

class Message(models.Model):

    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.score >= 70:
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body=f"Congratulations! {self.name} has scored {self.score} in the quiz. You are not a certified Python Programmer.",
                                from_='',
                                to=''
                            )

            print(message.sid)

        else:
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body=f"Sorry! {self.name} has scored {self.score} in the quiz. You are now a certified Python Programmer.",
                                from_='+17278558096',
                                to='+8801643257542'
                            )

            print(message.sid)


            super().save(*args, **kwargs)
