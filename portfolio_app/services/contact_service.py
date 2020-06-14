from portfolio_app import db, mail
from portfolio_app.models.contact_message import ContactMessage
from flask_mail import Message
from flask import current_app


def save_message(email_id, email_subject, email_content):
    db.session.add(ContactMessage(email_id, email_subject, email_content))
    db.session.commit()


def notify(email_id, email_subject, email_content):
    msg = Message(f"Message from portfolio app: {email_subject}.",
                  sender=current_app.config["MAIL_USERNAME"],
                  recipients=["sprasad3101@gmail.com"])
    msg.body = f"Email: {email_id}\n\nEmail Subject: {email_subject}\n\nEmail Content: {email_content}\n\n"
    mail.send(msg)