import pathlib
import json

home_dir = pathlib.Path.home()

config_dir = pathlib.Path(home_dir, '.gtu')
config_file = pathlib.Path(config_dir, 'config.json')

DEFAULT_FILE_PERSISTENCE_BASE = pathlib.Path(config_dir, 'tasks')

def init():
    if not config_dir.exists():
        config_dir.mkdir()
    if config_file.exists():
        config_file.unlink()
    return str(config_file)

def write(file_persistence_base):
    if not file_persistence_base:
        file_persistence_base = DEFAULT_FILE_PERSISTENCE_BASE
    config = {
        'file_persistence_base': str(file_persistence_base)
    }
    with config_file.open('a') as f:
        config_str = json.dumps(config, indent=2)
        f.write(config_str)
        return config_str

def load():
    return json.loads(get_str())

def get_str():
    with config_file.open('r') as f:
        return f.read()
