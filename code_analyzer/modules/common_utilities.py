def make_list_flat(_list):
    return sum(_list, [])

def is_special_marked(word):
    return word.startswith('__') and word.endswith('__')

def get_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        return file_handler.read()