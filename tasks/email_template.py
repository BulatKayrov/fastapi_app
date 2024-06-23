from email.message import EmailMessage
from config import settings


def create_email(email_to: str):
    msg = EmailMessage()
    msg['Subject'] = "Subject: Подтверждение"
    msg['From'] = settings.SMTP_USER
    msg['To'] = email_to
    msg.set_content('Просто контент . Смотри на него 30 мин и глаза перестанут болеть ))))')
    return msg

