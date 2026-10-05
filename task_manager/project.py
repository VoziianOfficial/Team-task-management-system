class Project:
    """
    Represents a project with tasks.
    """

    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.status = "active"

    def add_task(self, task):
        if self.status != "active":
            return False

        self.tasks.append(task)
        return True

    def show_tasks(self):
        for task in self.tasks:
            task.show_info()

    def calculate_progress(self):
        if not self.tasks:
            return 0

        done_tasks = 0

        for task in self.tasks:
            if task.status == "done":
                done_tasks += 1

        return int((done_tasks / len(self.tasks)) * 100)

    def close_project(self):
        if not self.tasks:
            return False

        for task in self.tasks:
            if task.status != "done":
                return False

        self.status = "closed"
        return True
