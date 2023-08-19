import datetime
from colorama import Style, Back, Fore

class Milestone (object):
    def __init__ (self, s):
        self.content = s
        self.date = datetime.date.today()

    def __str__ (self):
        out = f"[ON: {self.date}] {Style.BRIGHT}{self.content}{Style.RESET_ALL}"
        return out

class Project (object):
    def __init__ (self, name, tasks=[], description="", milestones=[]):
        self.name = name
        self.tasks = tasks
        self.desciription = description
        self.milestones = milestones
        self.started_on = datetime.date.today()

        self.add_milestone("Started working on the project")

    def add_milestone (self, milestone_str):
        self.milestones.append(Milestone(milestone_str))

    def complete_task (self, idx):
        del self.tasks[idx]

    def add_task (self, task):
        self.tasks.append(task)

    def __str__ (self):
       out = f"{Style.BRIGHT}{Back.GREEN}{Fore.BLACK}{self.name.upper()}{Fore.RESET}{Style.RESET_ALL}\n\n{Fore.YELLOW}Latest Milestone{Fore.RESET}\n• {self.milestones[-1]}\n\nTasks to do\n"
       out += "\n".join([f"{i+1}) {task}" for i,task in enumerate(self.tasks)])
       return out
