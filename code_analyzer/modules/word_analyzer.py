from modules.code_languages.python import get_names as get_names_python
from modules.code_languages.python import get_searching_places_dictionary as get_searching_places_dictionary_python

def get_code_languages_dictionary():
    code_languages = {'python': (get_names_python, get_searching_places_dictionary_python)}
    return code_languages

def check_code_languages(code_language):
    code_languages = get_code_languages_dictionary()
    if code_language in code_languages:
        return True
    else:
        return False

def get_names(files_paths, searching_place, code_language):
    code_languages_dictionary = get_code_languages_dictionary()
    get_words_function = code_languages_dictionary[code_language][0]
    names = get_words_function(files_paths, searching_place)
    return names

def check_and_get_searching_functon_name(searching_place, code_language):
    searching_functons_names = get_searching_places_dictionary(code_language)
    if searching_place in searching_functons_names:
        searching_functon_name = searching_functons_names[searching_place]
        return searching_functon_name
    else:
        return False

def get_searching_places_dictionary(code_language):
    code_languages_dictionary = get_code_languages_dictionary()
    searching_functons_names = code_languages_dictionary[code_language][1]
    return searching_functons_names()