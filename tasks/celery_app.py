from celery import Celery

from config import settings

app = Celery(
    main='celery',
    broker=settings.broker_url,
    backend=settings.backend_url,
    include=['tasks.user_tasks']
)


# @app.task
# def send_message(email: str):
#     content = create_email(email)
#
#     with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
#         server.ehlo()
#         server.starttls()
#         server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
#         server.send_message(from_addr=settings.SMTP_USER, to_addrs=email, msg=content)
#         server.quit()
