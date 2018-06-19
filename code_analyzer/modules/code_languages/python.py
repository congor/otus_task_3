import ast
from modules.common_utilities import get_file_content
from modules.common_utilities import make_list_flat
from modules.searching_places.function_names import get_function_names
from modules.searching_places.variables_names import get_variables_names

def get_names(files_paths, searching_place):
    files_syntax_nodes = get_syntax_nodes(files_paths)
    names = get_names_internal(files_syntax_nodes, searching_place)
    return names

def get_syntax_nodes(files_paths, with_filenames=False, with_file_content=False):
    nodes = []
    for file_path in files_paths:
        file_content = get_file_content(file_path)
        try:
            file_nodes = ast.parse(file_content)
        except SyntaxError:
            continue
        if with_filenames:
            if with_file_content:
                nodes.append((file_path, file_content, file_nodes))
            else:
                nodes.append((file_path, file_nodes))
        else:
            nodes.append(file_nodes)
    return nodes

def get_names_internal(files_syntax_nodes, searching_place):
    searching_functon_name = check_and_get_searching_functon_name(searching_place)    
    if searching_functon_name:
        return make_list_flat([get_names_from_node(file_nodes, searching_functon_name) for file_nodes in files_syntax_nodes])
    else:
        return []

def check_and_get_searching_functon_name(searching_place):
    searching_functons_names = get_searching_places_dictionary()    
    if searching_place in searching_functons_names:
        searching_functon_name = searching_functons_names[searching_place]
        return searching_functon_name
    else:
        return False

def get_searching_places_dictionary():
    searching_functons_names = {'functions': get_function_names,
                                'variables': get_variables_names
                               }
    return searching_functons_names

def get_names_from_node(file_nodes, searching_functon_name):
    return make_list_flat([get_places_content(searching_functon_name, node) for node in ast.walk(file_nodes)])

def get_places_content(searching_functon, node):
    return searching_functon(node)