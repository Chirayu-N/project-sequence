class Task:
    def __init__(self, id, name, duration, dependencies=[]):
        self.id = id
        self.name = name
        self.duration = duration
        self.dependencies = dependencies

        self.earliest_start = 0
        self.earliest_finish = 0
        self.latest_start = 0
        self.latest_finish = 0

        self.slack = 0
    
    def add_dependency(self, task):
        self.dependencies.append(task)

