from marketing_firm_creator import MarketingFirmCreator
import user_interface
from contestant import Contestant
import random


class Simulation:
    def __init__(self):
        pass

    @staticmethod
    def run_simulation():
        mark = MarketingFirmCreator()
        firm = mark.choose_manager_type()

        while True:
            userinput = user_interface.simulation_main_menu()
            if userinput == 1:
                new_contest = firm.manager.get_sweepstakes()
                while True:
                    userinput = user_interface.menu_2()
                    if userinput == 1:
                        reg_num = random.randint(100000, 999999)
                        contestant = user_interface.assign_contestant_info()
                        contestant = Contestant(contestant["firstname"],
                                                contestant["lastname"],
                                                contestant['email'],
                                                reg_num)
                        new_contest.register_contestant(contestant)
                    elif userinput == 2:
                        new_contest.pick_winner()
                        break
                    elif userinput == 3:
                        quit()
            elif userinput == 2:
                firm.create_sweepstakes('')
            elif userinput == 3:
                quit()
