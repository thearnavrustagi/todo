import pickle

from constants import TM_PATH, NORMAL
from task import Task
from project import Project

class TaskManager (object):
    def __init__ (self):
        self.tasks = []
        self.projects = {}

    @staticmethod
    def load (fname=TM_PATH):
        with open (fname, 'rb') as f:
            return pickle.load (f)

    def save (self,fname=TM_PATH):
        with open (fname, 'wb') as f:
            pickle.dump (self,f)

    def add_task (self, task, due, tag=NORMAL):
        self.tasks.append(Task(task, due, tag))

    def add_project_milestone (self,key,value):
        self.projects[key.lower().strip()].add_milestone (value)

    def complete_task (self, task_no):
        del self.tasks[task_no -1]

    def add_project_task (self, name, task, date, tag=NORMAL):
        name = name.lower().strip()
        task = Task(task, date, tag)
        self.projects[name].add_task(task)

    def add_project (self, project_name):
        project_name = project_name.lower().strip()
        self.projects[project_name] = Project(project_name)

    def complete_project_task (self, project_name, idx):
        project_name = project_name.lower().strip()
        self.projects[project_name].complete_task(idx-1)

    def __str__ (self):
        out = "Here are your tasks :\n"
        out += "\n".join([f"{i+1}) {task}" for i,task in enumerate(self.tasks)])
        out += "\n\n\nHere are your projects :\n"
        out += "\n".join([str(project) for _,project in self.projects.items()])

        return out

if __name__ == "__main__":
    print()
