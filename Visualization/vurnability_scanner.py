import ast
import astor
import re
import os

SQL_FUNCTIONS = {
    'execute',
    'executemany',
}
SQL_OPERATORS = re.compile('SELECT|UPDATE|INSERT|DELETE', re.IGNORECASE)


class ASTWalker(ast.NodeVisitor):
    def __init__(self):
        self.candidates = []
        self.variables = {}

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and node.func.attr in SQL_FUNCTIONS:
            self._check_function_call(node)
        self.generic_visit(node)

    def visit_Assign(self, node):
        if not isinstance(node.targets[0], ast.Name):
            return self.generic_visit(node)

        variable, value = node.targets[0].id, node.value
        if isinstance(value, (ast.Call, ast.BinOp, ast.Mod)):
            self.variables[variable] = node.value
        self.generic_visit(node)

    def _check_function_call(self, node):
        if not node.args:
            return
        first_argument = node.args[0]
        query = self._check_function_argument(first_argument)
        if query and re.search(SQL_OPERATORS, query):
            self.candidates.append(node)

    def _check_function_argument(self, argument):
        query = None
        if isinstance(argument, ast.Call) and argument.func.attr == 'format':
            query = argument.func.value.s
        elif isinstance(argument, ast.BinOp) and isinstance(argument.op, ast.Mod):
            query = argument.left.s
        elif isinstance(argument, ast.JoinedStr) and len(argument.values) > 1:
            query = argument.values[0].s
        elif isinstance(argument, ast.Name) and argument.id in self.variables:
            query = self._check_function_argument(self.variables[argument.id])
        return query


def scan_for_sql():
    root_dir = 'GitDownloads'
    list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".java"):
                code = open(os.path.join(root, file), 'r').read()
                try:
                    tree = ast.parse(code)
                    ast_walker = ASTWalker()
                    ast_walker.visit(tree)

                    for candidate in ast_walker.candidates:
                        list.append((file, astor.to_source(candidate).strip()))
                except:
                    print("pass")

    return list

# li = scan_for_sql()
# print(li)
