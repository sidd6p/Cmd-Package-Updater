import base64
import json
import requests
import csv
import os

from . import Repo
from dotenv import load_dotenv

load_dotenv()


##################################################################################################
def getUserRepoName(url):
    '''
        Returns the Username and Repo name from the given url

        Parameters:
            url (string): url for the given repo

        Returns:
            UserRep (dict): "user_name" and "repo_name" as string
            None: for unexpected input or behaviour
    '''

    try:
        data = url.split("/")
        user_rep = {"user": "", "repo": ""}
        
        idx = len(data) - 1
        while (idx >= 0):
            if (len(data[idx]) != 0):
                user_rep["user"] = data[idx - 1]
                user_rep["repo"] = data[idx]
                return user_rep
            idx -= 1
        return None
    except:
        return None
##################################################################################################



##################################################################################################
def getContent(repo):
    '''
        Returns the content of the package.json of the given repo

        Parameters:
            repo (dict): {"user": "", "repo": ""}
                
        Returns:
            json_data (dict): dict format of the package.json
            None: for unexpected input or behaviour
    '''

    try:
        request_url = "https://api.github.com/repos/{0}/{1}/contents/{2}".format(repo["user"], repo["repo"], "package.json")
        header = {
            'Authorization': 'token ' + os.getenv('PAT'),
            "Content-Type": "application/vnd.github.v3+json"
        }
        req = requests.get(request_url, headers=header)
        
        if req.status_code == requests.codes.ok:
            req = req.json()
            content = base64.b64decode(req['content'])
            json_string = content.decode('utf-8')
            json_data = json.loads(json_string)
            return json_data
        else:
            return None
    except:
        return None
##################################################################################################



##################################################################################################
def findVersion(data, dependency_name):
    '''
        Returns the version of the given dependency

        Parameters:
            repo (dict): {"user": "", "repo": ""}
            dependency_name (str): name of the dependency
                
        Returns:
            dependencies[dependency_name][1:] (str): verison of the given dependency in package.json file
            None: for unexpected input or behaviour
    '''

    try:
        dependencies = data["dependencies"]
        return dependencies[dependency_name][1:]
    except: 
        return None
##################################################################################################



##################################################################################################
def read(file_name):
    '''
        Returns the rows in .csv file data as list

        Parameters:
            file_name (str): .csv file
                
        Returns:
            data (list): list containing all row as items
    '''

    try:
        data = []

        with open(file_name, 'r') as input_file:
            csv_reader = csv.reader(input_file)

            for line in csv_reader:
                data.append(list(line))

        return data
    except:
        return None
##################################################################################################



##################################################################################################
def show(repos, dependency_version):
    '''
        Print the result in table format

        Parameters:
            repos (list): contain Repo objects
            dependency_version (str): required version of dependency
                
        Returns:
            NULL
    '''
    try:
        print("{:<30} | {:<55} | {:<10} | {:<30}".format("name", "repo", "version", "version_satisfied"))
        print("_"*130)
        print("")

        for repo in repos:
            name, url, version, version_satisfied = repo.name, repo.url, repo.version, "False"
            if repo.version >= dependency_version:
                version_satisfied = "True"
            print("{:<30} | {:<55} | {:<10} | {:<30}".format(name, url, version, version_satisfied))
    except:
        pass
##################################################################################################



##################################################################################################
def updateRepo(repos):
    '''
        Update the package.json file in repo with version less than given version

        Parameters:
            repos (list): contain Repo objects
                
        Returns:
            success (boolean): True if forking, updating and pull request get created successful else false
    '''

    try:
        success = True

        for repo in repos:
            if (repo.version < Repo.Repo.dependency["version"]):
                if (fork(repo)):
                    print("forked")
                    if (makeChanges(Repo.Repo.dependency, repo) != False):
                        print("changed")
                        if makeCommit(repo):
                            print("commited")
                            if (pullRequest(repo)) != False:
                                print("commited")
                                return success
                            else:
                                success = False
                        else:
                            success = False
                else:
                    success = False

        return success
    except:
        return False
##################################################################################################



##################################################################################################
def fork(repo):
    '''
        fork the required repo 

        Parameters:
            repo (Repo object): repo need to be forked
                
        Returns:
            success (boolean): True if forking is successful else False
    '''

    try:
        url = "https://api.github.com/repos/{0}/{1}/forks".format(repo.repo["user"], repo.repo["repo"])
        header = {
            'Authorization': 'token ' + os.getenv('PAT'),
            "Content-Type": "application/vnd.github.v3+json"
        }

        res = requests.post(url, headers=header)
        if (res.status_code != 202):
            return False
        else: 
            return True 
    except:
        return False
##################################################################################################



##################################################################################################
def makeChanges(dependency, repo):
    '''
        update the content of the repo object with new vesion

        Parameters:
            dependency (dic): {"name": "", "dependency": ""}
            repo (Repo Obj): repo
                
        Returns:
            success (boolean): True if update is successful else False
    '''
    
    try:
        initial = repo.content["dependencies"][dependency["name"]][0]
        if (initial.isnumeric() == False and initial != '.'):
            new_version = initial + dependency["version"]
        repo.content["dependencies"][dependency["name"]] = new_version
        return True
    except:
        return False
##################################################################################################



##################################################################################################
def makeCommit(repo):
    try:
        content = repo.content
        content = json.dumps(content)
        content = content.encode('utf-8')
        content = base64.b64encode(content)

        request_url = "https://api.github.com/repos/{0}/{1}/contents/{2}".format(os.getenv('USER_NAME'), repo["repo"], "package.json")
        header = {
            'Authorization': 'token ' + os.getenv('PAT'),
            "Content-Type": "application/vnd.github.v3+json"
        }
        body = {
            "message": "Updated the package.json",
            "content": content
        }

        res = requests.put(request_url, headers=header, data=body)
        if (res.status_code == 200):
            return True
        else: 
            return False
    except:
        return False
##################################################################################################



##################################################################################################
def pullRequest(repo):
    '''
        create pull request 

        Parameters:
            repo (Repo Obj): repo
                
        Returns:
            success (boolean): True if commit is successful else False
    '''
    pass
##################################################################################################
