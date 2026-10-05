class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.active_tasks = []

    def show_info(self):
        print(f"Employee: {self.name}")
        print(f"Role: {self.role}")
        print(f"Active tasks: {len(self.active_tasks)}")


    def add_task(self, task):
        self.active_tasks.append(task)

    def remove_task(self, task):
        if task in self.active_tasks:
            self.active_tasks.remove(task)
        else:
            print(f"Task '{task}' not found in active tasks.")
            
