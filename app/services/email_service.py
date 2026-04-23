from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.config import settings
import logging

logger = logging.getLogger(__name__)

async def send_email(
    to_email: str,
    subject: str,
    html_content: str
) -> bool:
    try:
        sg = SendGridAPIClient(settings.sendgrid_api_key)
        message = Mail(
            from_email=settings.notify_from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )
        sg.send(message)
        logger.info(f"Email sent to {to_email}: {subject}")
        return True
    except Exception as e:
        logger.error(f"Email failed: {str(e)}")
        return False
