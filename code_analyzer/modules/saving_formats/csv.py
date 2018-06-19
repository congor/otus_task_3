import os
import csv

def save_csv(results_file_path, data):
    with open(os.path.join(results_file_path), 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)