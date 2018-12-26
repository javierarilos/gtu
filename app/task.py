import json

class Task:
    def __init__(self, title, description='', due=None, tags=None):
        self.title = title
        self.description = description
        self.due = due
        self.tags = tags or ['inbox']

    def serialize(self):
        return json.dumps(self.__dict__, indent=2)

    @staticmethod
    def deserialize(json_str):
        t = Task('')
        t.__dict__ = json.loads(json_str)
        return t
