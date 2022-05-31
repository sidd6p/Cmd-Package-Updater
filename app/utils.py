import base64
import json
import requests

def getUserRepoName(url):
    data = url.split("/")
    userName = ""

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