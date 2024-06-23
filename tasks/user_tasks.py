import smtplib

from config import settings
from tasks.celery_app import app
from tasks.email_template import create_email


@app.task
def send_message(email: str):
    content = create_email(email)

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(from_addr=settings.SMTP_USER, to_addrs=email, msg=content)
        server.quit()