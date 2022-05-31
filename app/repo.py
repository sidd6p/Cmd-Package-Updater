import utils

class Repo:
    dependency = None
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.repo = utils.getUserName(self.url)
        self.version = utils.findVersion(self.repo, Repo.dependency["name"])
        self.version_greater = self.isGreater()
            
    def isGreater(self):
        return self.version >= Repo.dependency["version"]

    def __str__(self):
        return "{} {} {}".format(self.repo["user"], self.repo["repo"], self.version_greater)

    