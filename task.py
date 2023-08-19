from colorama import Fore,Back, Style
import datetime

from constants import NORMAL, URGENT

class Task (object):
    def __init__ (self, task, due, tag=NORMAL):
        self.task = task
        self.started = datetime.date.today()
        self.due = due
        self.tag = tag

    def __str__ (self):
        out = f"[DUE {self.due}] {Back.RESET} : {Style.BRIGHT}{self.task} {Style.RESET_ALL}"
        if self.tag == URGENT:
            out = Back.RED + out
        return out


