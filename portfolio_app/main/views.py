from flask import render_template, request, redirect, flash, url_for
from portfolio_app import profile
from portfolio_app.main import bp
from portfolio_app.services import contact_service
from portfolio_app.validators.validator import EmailValidator, TextValidator, validate


@bp.route('/')
def index():
    return render_template('index.html', skills=profile.get_skills(), outside_work_images=profile.outside_work_images())


@bp.route("/contact", methods=["POST"])
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

    return redirect(url_for("main.index", _anchor="contact-section"))


@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@bp.app_errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500