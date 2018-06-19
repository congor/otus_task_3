import ast
from modules.common_utilities import make_list_flat
from modules.common_utilities import is_special_marked

def get_variables_names(node):    
    variables_names = []
    if isinstance(node, ast.FunctionDef):
        for code_string in node.body:
            if isinstance(code_string, ast.Assign):                
                names = get_variables_name_from_code_string(code_string)
                variables_names.append(names)
    elif isinstance(node, ast.Assign):
        names = get_variables_name_from_code_string(node)
        variables_names.append(names)
    variables_names = make_list_flat(variables_names)    
    return variables_names

def get_variables_name_from_code_string(code_string):
    names = []
    for variable_name in code_string.targets:        
        try:
            variable_name = variable_name.id
            if not is_special_marked(variable_name):            
                names.append(variable_name)
        except:
            continue
    return names