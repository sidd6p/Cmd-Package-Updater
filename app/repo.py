from . import utils



class Repo:
    '''
        This is the class for storing repo in the form of object, so that it can be pass to 
        different function with all needed properties

        Class attribute:
            dependency (dict): {"name" : "", "version": ""}

        Class methods:
            __init__(self, name, url)
            __str__(self)

    '''
    dependency = None
    update = False

    ##################################################################################################
    def __init__(self, name, url):
        '''
            The constructor of Repo class

            Parameters:
                name (str): name of the given url
                url (str): url
        '''
        self.name = name or None
        self.url = url or None
        self.repo = utils.getUserRepoName(self.url) or None
        self.content = utils.getContent(self.repo) or None
        self.version = utils.findVersion(self.content,  Repo.dependency["name"]) or None
        self.pull_request = None
    ##################################################################################################


    ##################################################################################################
    def __str__(self):
        '''
            Print object
        '''
        return "{} {} {}".format(self.repo["user"], self.repo["repo"], self.version >= Repo.dependency["version"])
    ##################################################################################################

    