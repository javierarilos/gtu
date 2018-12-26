from os import path

gtu_dir = '/Users/jarias/gtu'


def get_fname(task):
    return task.title.replace(' ', '_') + '.task'

def save(task):
    file_abs_path = path.join(gtu_dir, get_fname(task))
    with open(file_abs_path, 'a') as f:
        f.write(task.serialize())
