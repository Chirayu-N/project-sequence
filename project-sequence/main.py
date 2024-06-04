
class Task:
    def __init__(self, id: int, name: str, duration: float) -> None:
        self.id = id
        self.name = name
        self.duration = duration
        self.dependencies = []

        self.earliest_start = 0
        self.earliest_finish = 0
        self.latest_start = 0
        self.latest_finish = 0

        self.slack = 0
    
    def add_dependency(self, task_id: int) -> None:
        self.dependencies.append(task_id)


class Project:
    def __init__(self) -> None:
        self.tasks = dict()  
    

    def add_task(self, task: Task):
        self.tasks[task.id] = task
    

    def add_dependency(self, task_id: int, dependency_id: int):
        self.tasks[task_id].add_dependency(dependency_id)
    

    def find_critical_path(self):
        pass # TODO


if __name__ == '__main__':
    task = Task(0, "Task", 10.0)
    task.add_dependency(1)
    print(task.dependencies)