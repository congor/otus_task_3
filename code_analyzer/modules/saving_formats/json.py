import os
import json
import codecs

def save_json(results_file_path, data):
    with open(os.path.join(results_file_path), 'wb') as file:
        json.dump(data, codecs.getwriter('utf-8')(file), ensure_ascii=False)