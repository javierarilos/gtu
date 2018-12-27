import json
import re

class Task:
    def __init__(self, title, description='', tags=None, due=None):
        self.title = title
        self.description = description
        self.due = due
        self.tags = tags or ['inbox']

    def serialize(self):
        return json.dumps(self.__dict__, indent=2)

    @staticmethod
    def deserialize(json_str):
        t = Task('')
        try:
            t.__dict__ = json.loads(json_str)
        except:
            print('Error deserializing ' + json_str)
            raise
        return t

    @staticmethod
    def from_multiline(task_str):
        lines = task_str.splitlines()
        title = lines[0]
        if len(lines) > 0:
            description = '\n'.join(lines[1:])
        else:
            description = ''

        regex = r"#(\w+)"
        tags = list({m for match in re.finditer(regex, task_str, re.MULTILINE) for m in match.groups()})
        return Task(title, description=description, tags=tags)
