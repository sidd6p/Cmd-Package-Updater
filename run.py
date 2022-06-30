import getopt, sys
from app import utils, Repo


args_list = sys.argv[1:]

options = "i:u"
long_option = ["input=", "update"]

try:
    arguments, values = getopt.getopt(args_list, options, long_option)
    dependency = {"name": sys.argv[-1].split("@")[0], "version": sys.argv[-1].split("@")[1]}
    Repo.Repo.dependency = dependency
    data = None
    repos = []

    for current_arguments, current_values in arguments:
        if (current_arguments.lower() in ("-i", "--input")):
            data = utils.read(current_values)[1:]
        elif (current_arguments.lower() in ("-u", "--update")):
            Repo.Repo.update = True
    
    for i in data:
        item = Repo.Repo(i[0], i[1])
        repos.append(item)
    
    if (Repo.Repo.update == True):
        utils.updateRepo(repos)
    
    utils.show(repos, dependency["version"])


except getopt.error as error:
    print (str(error))
