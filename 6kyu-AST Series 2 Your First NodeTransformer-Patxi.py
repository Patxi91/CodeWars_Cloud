import ast

class YourFirstNodeTransformer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        # Check if the function name is "_"
        if node.name == "_" or node.name.startswith("manipulate"):
            # Visit the body of the function and apply the transformation
            node.body = [self.visit(stmt) for stmt in node.body]
        return node

    def visit_BinOp(self, node):
        # Check if the operation is addition
        if isinstance(node.op, ast.Add):
            # Replace the addition with a constant value of 5
            return ast.copy_location(ast.Num(n=5), node)
        return node

def _():
    return 2 + 2
