from modules.load_settings import load_settings
from modules.utilities import check_posibility
from modules.utilities import get_file_paths
from modules.word_analyzer import get_names
from modules.speech_part_analyzer import filter_words
from modules.utilities import get_most_frequent_words
from modules.save_results import output_results
from modules.utilities import print_results_to_console

if __name__ == '__main__':
    settings = load_settings()
    if settings and check_posibility(settings):
        words_statistics = []
        for project_path in settings.projects_paths:
            files_paths = get_file_paths(project_path)            
            names = get_names(files_paths, settings.searching_place, settings.code_language)
            filtered_words = filter_words(names, settings.part_of_speech)
            words_statistics += get_most_frequent_words(filtered_words, 10)
        output = [(attached_tags[0], attached_tags[1]) for attached_tags in get_most_frequent_words(words_statistics, 200)]
        output_results(output, settings.saving_format)
        print_results_to_console(output)
        print('Done')
    else:
        print('An error has been detected, the application is stopped')