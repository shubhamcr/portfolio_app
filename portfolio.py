from portfolio_app import create_app, db
from portfolio_app.models import contact_message

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'ContactMessage': contact_message.ContactMessage}
