import utils


class Task:
    """
    Represents a project task.
    """

    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

        self.status = "new"
        self.assignee = None
        self.task_id = utils.generate_task_id()
        self.created_at = utils.get_current_time()

    def show_info(self):
        print(f"Task ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")

        if self.assignee is None:
            print("Assignee: Not assigned")
        else:
            print(f"Assignee: {self.assignee.name}")

    def assign_to(self, employee):
        self.assignee = employee
        employee.add_task(self)
        self.status = "assigned"

    def start(self):
        if self.assignee is None:
            return False, "Task cannot be started without an assignee."

        if self.status != "assigned":
            return False, "Task cannot be started."

        self.status = "in_progress"
        return True, "Task started successfully."

    def complete(self):
        if self.status != "in_progress":
            return False, "Task cannot be completed if it is not in progress."

        self.status = "done"
        self.assignee.remove_task(self)

        return True, "Task completed successfully."
