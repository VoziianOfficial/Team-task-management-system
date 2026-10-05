def find_task(tasks, task_id):
    for task in tasks:
        if task.task_id == task_id:
            return task

    return None


def show_tasks_by_status(tasks, status):
    for task in tasks:
        if task.status == status:
            task.show_info()


def count_tasks_by_status(tasks):
    result = {"new": 0, "assigned": 0, "in_progress": 0, "done": 0}

    for task in tasks:
        result[task.status] += 1

    return result
