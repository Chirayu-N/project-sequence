from collections import deque

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
    

    def add_task(self, task: Task) -> None:
        self.tasks[task.id] = task
    

    def add_dependency(self, task_id: int, dependency_id: int) -> None:
        self.tasks[task_id].add_dependency(dependency_id)
    

    def topological_sort(self):
        indegree = {task.id: 0 for task in self.tasks.values()}
        for task in self.tasks.values():
            for dep in task.dependencies:
                indegree[dep.id] += 1

        queue = deque([task.id for task in self.tasks.values() if indegree[task.id] == 0])
        topo_order = []

        while queue:
            current_id = queue.popleft()
            topo_order.append(current_id)
            for dep in self.tasks[current_id].dependencies:
                indegree[dep.id] -= 1
                if indegree[dep.id] == 0:
                    queue.append(dep.id)

        return topo_order

    def find_critical_path(self) -> list:
        topo_order = self.topological_sort()

        # Forward pass
        for task_id in topo_order:
            task = self.tasks[task_id]
            if not task.dependencies:
                task.earliest_start = 0
            else:
                task.earliest_start = max(dep.earliest_finish for dep in task.dependencies)
            task.earliest_finish = task.earliest_start + task.duration

        # Backward pass
        reverse_topo_order = reversed(topo_order)
        max_earliest_finish = max(self.tasks[task_id].earliest_finish for task_id in topo_order)
        
        for task_id in reverse_topo_order:
            task = self.tasks[task_id]
            if not any(dep for dep in self.tasks.values() if task in dep.dependencies):
                task.latest_finish = max_earliest_finish
            else:
                task.latest_finish = min(dep.latest_start for dep in self.tasks.values() if task in dep.dependencies)
            task.latest_start = task.latest_finish - task.duration
            task.slack = task.latest_start - task.earliest_start

        # Identify the critical path
        critical_path = [task for task in self.tasks.values() if task.slack == 0]
        return critical_path


if __name__ == '__main__':
    tasks = [Task(0, "Task0", 0.0), Task(1, "Task1", 10.0), Task(2, "Task2", 20.0)]
    project = Project()
    for task in tasks:
        project.add_task(task)
    
    dependencies = {0: [], 1: [0], 2: [0, 1]}
    for task_key in dependencies.keys():
        for dependency_id in dependencies[task_key]:
            project.add_dependency(task_key, dependency_id)
    
    print(project.tasks[2].dependencies)