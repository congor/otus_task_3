import ast
from modules.common_utilities import is_special_marked

def get_function_names(node):
    function_name = []
    if isinstance(node, ast.FunctionDef) and not is_special_marked(node.name):
        function_name.append(node.name.lower())
    return function_name