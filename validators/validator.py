from validate_email import validate_email


def validate(validator):
    return validator.validate()


class Validator:
    def __init__(self, field):
        self.field = field

    def validate(self):
        pass


class EmailValidator(Validator):
    def __init__(self, email: str):
        super(EmailValidator, self).__init__(email)

    def validate(self):
        return validate_email(email_address=self.field.strip(), check_regex=True, check_mx=True,
                              from_address='sprasad3101@gmail.com', helo_host='gmail.com', smtp_timeout=10,
                              dns_timeout=10, use_blacklist=True)


class TextValidator(Validator):
    def __init__(self, text: str):
        super(TextValidator, self).__init__(text)

    def validate(self):
        return self.field.strip()
