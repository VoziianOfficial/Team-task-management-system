from employee import Employee
from task import Task
from project import Project
import reports



backend = Employee("Yuliia", "Backend Developer")
frontend = Employee("Anna", "Frontend Developer")
designer = Employee("Max", "Designer")

employees = [backend, frontend, designer]

print("\n--- EMPLOYEES ---")

for employee in employees:
    employee.show_info()




project = Project("Online Shop Redesign")




task1 = Task(
    "Create database", "Create database structure for products and users", "high"
)

task2 = Task("Build login API", "Create login and registration API", "high")

task3 = Task("Build product page", "Create frontend product page", "medium")

task4 = Task("Implement checkout", "Create checkout interface", "high")

task5 = Task("Design homepage", "Create new homepage design", "medium")




project.add_task(task1)
project.add_task(task2)
project.add_task(task3)
project.add_task(task4)
project.add_task(task5)

print("\n--- PROJECT TASKS ---")

project.show_tasks()



task1.assign_to(backend)
task2.assign_to(backend)

task3.assign_to(frontend)
task4.assign_to(frontend)

task5.assign_to(designer)


print("\n--- CHECK ASSIGNEES ---")

print(task1.assignee.name)
print(task3.assignee.name)
print(task5.assignee.name)


print("\n--- CHECK ACTIVE TASKS ---")

print("Backend tasks:", len(backend.active_tasks))
print("Frontend tasks:", len(frontend.active_tasks))
print("Designer tasks:", len(designer.active_tasks))




print("\n--- EMPLOYEES AFTER ASSIGNMENT ---")

for employee in employees:
    employee.show_info()



task1.start()
task2.start()
task3.start()

print("\n--- AFTER START ---")

print(task1.title, "-", task1.status)
print(task2.title, "-", task2.status)
print(task3.title, "-", task3.status)
print(task4.title, "-", task4.status)
print(task5.title, "-", task5.status)



task1.complete()
task2.complete()

print("\n--- AFTER COMPLETE ---")

print(task1.title, "-", task1.status)
print(task2.title, "-", task2.status)

print("Backend active tasks:", len(backend.active_tasks))




progress = project.calculate_progress()

print("\n--- PROJECT PROGRESS ---")
print(f"Project progress: {progress}%")




stats = reports.count_tasks_by_status(project.tasks)

print("\n--- TASK STATISTICS ---")

for status, count in stats.items():
    print(f"{status}: {count}")




print("\n--- FIND TASK ---")

task_id = task3.task_id

found_task = reports.find_task(project.tasks, task_id)

if found_task is not None:
    print("Task found:")
    found_task.show_info()
else:
    print("Task not found")


not_found = reports.find_task(project.tasks, 999999)

print("Search 999999:", not_found)




print("\n--- TRY CLOSE PROJECT ---")

result = project.close_project()

print("Close result:", result)
print("Project status:", project.status)




# task3 уже in_progress
task3.complete()

# task4 и task5 пока assigned
task4.start()
task4.complete()

task5.start()
task5.complete()


progress = project.calculate_progress()

print("\n--- FINAL PROGRESS ---")
print(f"Project progress: {progress}%")




result = project.close_project()

print("\n--- CLOSE PROJECT ---")
print("Close result:", result)
print("Project status:", project.status)




new_task = Task("New task", "This task should not be added", "low")

result = project.add_task(new_task)

print("\n--- ADD TASK TO CLOSED PROJECT ---")
print("Add task result:", result)




print("\n--- OOP INFO ---")

print(type(task1))
print(isinstance(task1, Task))
print(vars(task1))
print(hasattr(task1, "status"))
print(getattr(task1, "priority"))

print(vars(backend))
print(vars(project))

print(Task.__doc__)
print(Employee.__doc__)
print(Project.__doc__)
