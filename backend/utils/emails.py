from django.conf import settings
from django.core.mail import EmailMessage

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Email(EmailMessage):

    def send(self, fail_silently=False):
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        message = Mail(
            from_email=self.from_email,
            to_emails=self.to,
            subject=self.subject,
            html_content=self.body
        )
        return sg.send(message)
