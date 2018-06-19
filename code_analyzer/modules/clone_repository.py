import os
from datetime import datetime
from urllib.parse import urlparse
from modules.remote_sources.git import git

def get_clone_function(source):
    clone_functions = {'github.com': git}
    return clone_functions.get(source)

def determine_source(project_url):
    parsed_url = urlparse(project_url)
    return parsed_url.netloc

def clone_repository(project_url):
    cloned_repositories_local_path = 'cloned_repositories'
    project_name = project_url.split('/')[-1] + '_' + str(datetime.now()).replace(':', '-')
    cloned_path = os.path.abspath(os.path.join(cloned_repositories_local_path, project_name))
    source = determine_source(project_url)
    clone_function = get_clone_function(source)
    if clone_function is None:
        print('{} is not supported as an remote repository'.format(source))
        return None    
    elif clone_function(project_url, cloned_path) is True:
        return cloned_path