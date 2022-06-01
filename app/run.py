import getopt, sys
import repo
import utils


args_list = sys.argv[1:]

options = "i:u"
long_option = ["input=", "update"]

try:
    arguments, values = getopt.getopt(args_list, options, long_option)
    dependency = {"name": sys.argv[-1].split("@")[0], "version": sys.argv[-1].split("@")[1]}
    repo.Repo.dependency = dependency
    data = None
    repos = []

    for current_arguments, current_values in arguments:
        if (current_arguments.lower() in ("-i", "--input")):
            data = utils.read(current_values)[1:]
        elif (current_arguments.lower() in ("-u", "--update")):
            print ("Updating the file....")
    for i in data:
        item = repo.Repo(i[0], i[1])
        repos.append(item)
    utils.show(repos, dependency["version"])


except getopt.error as error:
    print (str(error))
