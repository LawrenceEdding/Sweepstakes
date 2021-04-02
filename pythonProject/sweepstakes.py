from random import choice
import user_interface


class Sweepstakes:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self, contestant):
        self.contestants[contestant.registration_number] = contestant

    def pick_winner(self):
        winner = choice(list(self.contestants.keys()))
        for contestant in self.contestants.values():
            if contestant.registration_number == winner:
                contestant.notify(True)
            else:
                contestant.notify(False)

        return winner

    @staticmethod
    def print_contestant_info(contestant):
        user_interface.output_text(f'Name {contestant.first_name} {contestant.last_name}\n')
        user_interface.output_text(f'Email {contestant.email}\n')
