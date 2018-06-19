import os
import collections
from modules.word_analyzer import check_code_languages
from modules.word_analyzer import get_code_languages_dictionary
from modules.word_analyzer import check_and_get_searching_functon_name
from modules.word_analyzer import get_searching_places_dictionary
from modules.speech_part_analyzer import check_part_of_speech_analysis_availability
from modules.speech_part_analyzer import get_parts_of_speech_dictionary
from modules.save_results import check_and_get_saving_functon_name
from modules.save_results import get_saving_formats_dictionary

def check_posibility(settings):
    if not check_code_languages(settings.code_language):
        print('Incorrect input or "{}" as a code language is not supported'.format(settings.code_language))
        code_languages = get_code_languages_dictionary()
        print('Choose one of code languages for analysis and correct the settings json-file:')
        for code_language in code_languages:
            print(' - ', code_language)
        return False
    if not check_and_get_searching_functon_name(settings.searching_place, settings.code_language):
        print('Incorrect input or "{}" as a searching place is not supported for the "{}" code language'.format(settings.searching_place, settings.code_language))
        searching_places = get_searching_places_dictionary(settings.code_language)
        print('Choose one of searching places for analysis and correct the settings json-file:')
        for searching_place in searching_places:
            print(' - ', searching_place)
        return False
    if not check_part_of_speech_analysis_availability(settings.part_of_speech):
        print('Incorrect input or "{}" as a part of speach is not supported'.format(settings.part_of_speech))
        parts_of_speech_dictionary = get_parts_of_speech_dictionary()
        print('Choose one of available parts of speech for analysis and correct the settings json-file:')
        for part_of_speech in parts_of_speech_dictionary:
            print(' - {} - {}'.format(part_of_speech, parts_of_speech_dictionary[part_of_speech]))
        return False    
    if len(settings.projects_paths) == 0:
        print('There are not paths for analysis')
        print('Determine a correct project path and correct the settings json-file')
        return False
    if not check_and_get_saving_functon_name(settings.saving_format):        
        print('Incorrect input or "{}" as a saving file format is not supported'.format(settings.saving_format))
        saving_formats = get_saving_formats_dictionary()
        print('Choose one of saving formats for analysis and correct the settings json-file:')
        for saving_format in saving_formats:
            print(' - ', saving_format)
        print('Results will not be saved in any file')
    return True

def get_file_paths(project_path):
    filenames = []
    for dirname, dirs, files in os.walk(project_path, topdown=True):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
            if len(filenames) == 100:
                break
    return filenames

def get_most_frequent_words(verbs, top_size=10):
    return collections.Counter(verbs).most_common(top_size)

def print_results_to_console(data):
    print('Analysis results:')
    for output_string in data:
        print(output_string)