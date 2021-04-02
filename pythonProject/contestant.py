import user_interface


class Contestant:
    def __init__(self, fname, lname, email, reg_number):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.registration_number = reg_number  # TODO Make sure number is unique

    def notify(self, is_winner):
        if is_winner:
            text = 'win'
        else:
            text = 'lose'
        user_interface.output_text(f'{self.first_name} You {text}!')
