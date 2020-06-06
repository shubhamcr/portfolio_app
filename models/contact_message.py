from .. import db


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), index=True)
    subject = db.Column(db.String(), index=True)
    content = db.Column(db.String())

    def __repr__(self):
        return f'Email: {self.email}\nSubject: {self.subject}\nContent: {self.content}'