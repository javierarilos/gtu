import pathlib
from app import config
from app.task import Task

gtu_dir = None


def get_persistence_base_dir():
    cfg = config.load()
    gtu_dir = pathlib.Path(cfg['file_persistence_base'])
    if not gtu_dir.exists():
        gtu_dir.mkdir()
    return gtu_dir


def get_fname(task):
    return task.title.replace(' ', '_') + '.task'


def save(task):
    file_abs_path = pathlib.Path(get_persistence_base_dir(), get_fname(task))
    with file_abs_path.open('w+') as f:
        f.write(task.serialize())

def get_tasks():
    return [Task.deserialize(task_file.read_text()) for task_file in get_persistence_base_dir().glob('*.task')]
