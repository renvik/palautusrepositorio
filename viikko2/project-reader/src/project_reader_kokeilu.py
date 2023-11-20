import toml
from urllib import request

class Project:
    def __init__(self, name, description, dependencies, tasks):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.tasks = tasks

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Fetch the file content from the URL
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # Deserialize the TOML-formatted string and create a Project object based on its data
        parsed_toml = toml.loads(content)
        print(parsed_toml)

        # Assuming the TOML file has 'name', 'description', 'dependencies' and 'tasks' keys
        return Project(parsed_toml["name"], parsed_toml["description"], parsed_toml["dependencies"], parsed_toml["tasks"])