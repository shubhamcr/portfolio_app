from .. import db
from sqlalchemy import func


class ContactMessage(db.Model):
    __tablename__ = "ContactMessage"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), index=True, nullable=False)
    subject = db.Column(db.String(), index=True, nullable=False)
    content = db.Column(db.String(), nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'Email: {self.email}\nSubject: {self.subject}\nContent: {self.content}\nTime: {self.time_created}'