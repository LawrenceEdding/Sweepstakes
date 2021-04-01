class Contestant:
    def __init__(self, fname, lname, email, reg_number):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.registration_number = reg_number

    def notify(self, is_winner):
        if is_winner:
            pass
