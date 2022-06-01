from . import utils

class Repo:
    dependency = None
    update = False
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.repo = utils.getUserRepoName(self.url)
        self.version = utils.findVersion(self.repo, Repo.dependency["name"]) or "0.24.0" 

    def __str__(self):
        return "{} {} {}".format(self.repo["user"], self.repo["repo"], self.version >= Repo.dependency["version"])

    