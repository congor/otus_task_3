from git import Repo
from urllib.request import urlopen

def git(project_url, cloned_path):
    try:
        urlopen(project_url)
    except urllib.error.HTTPError:
        print('Repository on the link "{}" is not found or there is a problems with an Internet connection'.format(project_url))
        return False
    else:
        Repo.clone_from(project_url, cloned_path)
        print('The project "{}" has been cloned to "{}"'.format(project_url, cloned_path))
        return True