import app.local_file_persistence as persistence


def all_tasks():
    return persistence.get_tasks()


def save(task):
    return persistence.save(task)


def tasks_by_title():
    return {task.title: task for task in persistence.get_tasks()}


def all_tags():
    return set((tag for task in all_tasks() for tag in task.tags))


def tasks_tagged(tag):
    return [task for task in persistence.get_tasks() if tag in task.tags]
