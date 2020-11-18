from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task.name in map(lambda t: t.name, self.tasks):
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        tasks = [task.name for task in self.tasks]
        if task_name not in tasks:
            return f'Could not find task with the name {task_name}'

        task = self.tasks[tasks.index(task_name)]
        task.completed = True
        return f'Completed task {task_name}'

    def clean_section(self):
        completed_tasks = [task for task in self.tasks if task.completed]

        for task in completed_tasks:
            self.tasks.remove(task)

        return f'Cleared {len(completed_tasks)} tasks.'

    def view_section(self):
        section_details = [f'Section {self.name}:']
        task_details = [task.details() for task in self.tasks]
        return '\n'.join(section_details + task_details) + '\n'
