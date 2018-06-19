import os
from datetime import datetime
from modules.saving_formats.json import save_json
from modules.saving_formats.csv import save_csv

def get_saving_formats_dictionary():
    saving_formats = {'json': save_json,
                      'csv': save_csv,
                     }
    return saving_formats

def check_and_get_saving_functon_name(saving_format):    
    saving_formats = get_saving_formats_dictionary()
    if saving_format in saving_formats:
        saving_function = saving_formats[saving_format]
        return saving_function
    else:
        return False

def output_results(data, saving_format):    
    saving_function = check_and_get_saving_functon_name(saving_format)    
    if saving_function:    	
        results_file_path = create_results_file_path(saving_format)
        try:
            saving_function(results_file_path, data)
            print('Results have been saved in the file with the path "{}"'.format(results_file_path))
        except:
            print('An saving error has been detected, results have not been saved')

def get_result_folder_path():
    results_folder_name = 'results'
    results_folder_path = os.path.join(results_folder_name)
    if not os.path.isdir(results_folder_path):
        try:
            os.mkdir(results_folder_path)
        except:
            print("The result folder has not been created in '{}'".format(results_folder_path))
    return results_folder_path

def create_results_file_path(encode):    
    results_folder_path = get_result_folder_path()
    results_file_name = str(datetime.now()).replace(':', "-") + '.' + encode
    results_file_path = os.path.abspath(os.path.join(results_folder_path, results_file_name))
    return results_file_path