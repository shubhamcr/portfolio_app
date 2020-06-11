from flask import render_template, request, redirect, flash, url_for
from .portfolio import app
from . import profile
from .services import contact_service
from .validators.validator import EmailValidator, TextValidator, validate


@app.route('/')
def index():
    return render_template('index.html', skills = profile.get_skills())


@app.route("/contact", methods=["POST"])
def contact():
    email_id = (request.form['email_id']).strip()
    email_subject = (request.form['email_subject']).strip()
    email_content = (request.form['email_content']).strip()

    error = False

    if not validate(EmailValidator(email_id)):
        error = True
        flash("Enter a valid email.", "error")

    if not validate(TextValidator(email_subject)):
        error = True
        flash("Email subject cannot be empty.", "error")

    if not validate(TextValidator(email_content)):
        error = True
        flash("Email content cannot be empty.", "error")

    if not error:
        contact_service.save_message(email_id, email_content, email_subject)
        contact_service.notify(email_id, email_content, email_subject)
        flash("Thank you for contacting me. I have received your message and "
              "will get back to you shortly.", "message")

    return redirect(url_for("index", _anchor="contact-section"))