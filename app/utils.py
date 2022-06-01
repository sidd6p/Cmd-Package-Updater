import base64
import json
import requests
import csv
import Repo
import os

from dotenv import load_dotenv

load_dotenv()


def getUserRepoName(url):
    data = url.split("/")

    idx = len(data) - 1
    while (idx >= 0):
        if (len(data[idx]) != 0):
            user_name = data[idx - 1]
            repo_name = data[idx]
            return {"user": user_name, "repo": repo_name}
        idx -= 1
    return None
    


def findVersion(repo, dependency_name):
    request_url = "https://api.github.com/repos/{0}/{1}/contents/{2}".format(repo["user"], repo["repo"], "package.json")
    req = requests.get(request_url)
    
    if req.status_code == requests.codes.ok:
        req = req.json()
        content = base64.b64decode(req['content'])
        json_string = content.decode('utf-8')
        json_data = json.loads(json_string)
        dependencies = json_data["dependencies"]
        return dependencies[dependency_name][1:]
    else:
        return None



def read(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        csv_reader = csv.reader(input_file)

        for line in csv_reader:
            data.append(list(line))
    return data



def show(data, dependency_version):
    print("{:<30} | {:<55} | {:<10} | {:<30}".format("name", "repo", "version", "version_satisfied"))
    print("_"*130)
    print("")
    for row in data:
        name, repo, version, version_satisfied = row.name, row.url, row.version, "False"
        if row.version >= dependency_version:
            version_satisfied = "True"
        print("{:<30} | {:<55} | {:<10} | {:<30}".format(name, repo, version, version_satisfied))



def updateRepo(repos):
    for repo in repos:
        if (repo.version < Repo.Repo.dependency["version"]):
            if (fork(repo)):
                pullRequest()



def fork(repo):
    url = "https://api.github.com/repos/{0}/{1}/forks".format(repo.repo["user"], repo.repo["repo"])
    header = {
        'Authorization': 'token ' + os.getenv('PAT'),
        "Content-Type": "application/vnd.github.v3+json"
    }

    res = requests.post(url, headers=header)
    if (res.status_code != 200):
        return False
    else: 
        return True 



def pullRequest():
    pass