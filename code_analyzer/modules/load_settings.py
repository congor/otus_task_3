import os
import ast
import json
from modules.clone_repository import clone_repository

def load_settings():

    class Settings:
        def __init__(self, raw_settings):
            self.code_language = raw_settings.get('code_language')
            self.part_of_speech = raw_settings.get('part_of_speech')
            self.searching_place = raw_settings.get('searching_place')
            projects = raw_settings.get('projects')
            self.projects_paths = determine_projects_paths(projects)
            self.saving_format = raw_settings.get('saving_format')            

    try:
        with open('settings/settings.json', 'r', encoding='utf_8') as settings_file:
            raw_settings = json.load(settings_file)
    except FileNotFoundError:
        print('No one of settings-files is not founded')        
        default_settings = get_settings_titles_dictionary()
        settings = Settings(default_settings)
        print('Default settings for analysis will be used')
    except ValueError:
        print('The settings json-file contains invalid json. Correct the settings json-file')
        print("If you use Windows-style paths with backslash in the settings json-file, don't do that. Use the double backslash '\\' instead. This is the standard python json encoder requirement")
        return False
    else:
        test_folder_path = get_test_folder_projects_paths()
        if test_folder_path:
            default_settings = get_settings_titles_dictionary()
            default_settings['projects'] = test_folder_path
            settings = Settings(default_settings)
        elif check_settings_file_correctness(raw_settings):
            settings = Settings(raw_settings)
        else:
            settings = False
    if settings:
        print('Next settings have been read from the settings file:')
        print('* Code_language: {}'.format(settings.code_language))
        print('* Part of speech: {}'.format(settings.part_of_speech))
        print('* Searching place: {}'.format(settings.searching_place))
        print('* Projects paths:')        
        for project_path in settings.projects_paths:
            print(' - {}'.format(project_path))
        print('* Saving format: {}'.format(settings.saving_format))
    return settings

def check_settings_file_correctness(raw_settings):
    titles = get_settings_titles_dictionary()
    wrong_titles = []
    for variable in raw_settings:
        if not variable in titles:
            wrong_titles.append(variable)
    if len(wrong_titles) > 0:
        print('The settings json-file is not correct, because next titles have mistakes or necessary titles are absent:')
        for wrong_title in wrong_titles:
            print('- {}'.format(wrong_title))
        print('The settings json-file must have next necessary titles:')
        for title in titles:
            print('- {}'.format(title))
        return False
    else:
        return True

def get_settings_titles_dictionary():
    settings_titles_dictionary = {'code_language': 'python',
                                  'part_of_speech': 'VB',
                                  'searching_place':'functions',
                                  'projects': '.',
                                  'saving_format':'json',
                                  }
    return settings_titles_dictionary

def determine_projects_paths(projects):
    projects_paths = []
    for project in projects:
        if is_url(project):
            cloned_project_path = clone_repository(project)
            if cloned_project_path: projects_paths.append(cloned_project_path)
        else:
            project_path = check_and_get_local_project_path(project)
            if project_path: projects_paths.append(project_path)
    return projects_paths

def is_url(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def check_and_get_local_project_path(project):
    project_path = os.path.abspath(project)
    if not os.path.isdir(project_path):
        print('The path for project "{}" has not been found. Correct the settings json-file'.format(project))
    else:
        return project_path

def get_test_folder_projects_paths():
    test_folder = 'test_data'
    if os.path.isdir(os.path.join(test_folder)):
        print('Internal test mode. To avoid this mode - rename or remove "test_data" folder from the root application folder')
        return [os.path.join(test_folder, project) for project in os.listdir(test_folder) if os.path.isdir(os.path.join(test_folder, project))]