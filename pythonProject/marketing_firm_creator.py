from marketing_firm import MarketingFirm
from sweepstakes_queue import SweepstakesQueueManager as Queue
from sweepstakes_stack import SweepstakesStackManager as Stack


import user_interface


class MarketingFirmCreator:  # DONE Reference in simulation for testing.
    def __init__(self):
        self.firm = None

    def choose_manager_type(self):
        userinput = user_interface.choose_manager_type()
        if userinput == 1:
            self.firm = MarketingFirm(Stack())
        elif userinput == 2:
            self.firm = MarketingFirm(Queue())
        elif userinput == 3:
            quit()
        return self.firm
