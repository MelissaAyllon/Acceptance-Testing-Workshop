tasks = []


def add_task(task):
    tasks.append({
        "id": len(tasks) + 1,
        "title": task,
        "status": "Pending",
        "date": "2025-01-07"
    })


def list_tasks():
    if not tasks:
        return "No tasks in the to-do list."
    result = "Tasks:\n"
    for task in tasks:
        symbol = "✓" if task["status"] == "Completed" else "○"
        result += (
            f"- {symbol} [{task['id']}] {task['title']} ({task['status']})\n"
        )
    return result.strip()


def mark_completed(task_title):
    for task in tasks:
        if task["title"] == task_title:
            task["status"] = "Completed"
            return True
    return False


def clear_tasks():
    global tasks
    tasks = []


def delete_task(task_title):
    global tasks
    tasks = [task for task in tasks if task["title"] != task_title]


def search_tasks(keyword):
    return [task for task in tasks if keyword.lower() in task["title"].lower()]

