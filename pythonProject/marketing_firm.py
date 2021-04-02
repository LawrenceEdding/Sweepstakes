from sweepstakes import Sweepstakes


class MarketingFirm:
    def __init__(self, manager):  # Manager is Abstract data type of stack or queue
        self.manager = manager

    def create_sweepstakes(self, name):
        sweepstakes = Sweepstakes(name)
        self.manager.insert_sweepstakes(sweepstakes)
