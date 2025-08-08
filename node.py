import numpy as np

class Node:
    def __init__(self, node_type, value, left=None, right=None):
        """
        node_type: 'binary_op', 'unary_op', 'variable', 'constant'
        value: function (for ops), string (for variable e.g. 'x0'), or numeric (for constant)
        left/right: child nodes. For unary ops we store the child in .left.
        """
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right

    def clone_node(self):
        left_clone = self.left.clone_node() if self.left is not None else None
        right_clone = self.right.clone_node() if self.right is not None else None
        return Node(self.node_type, self.value, left_clone, right_clone)

    def to_string(self):
        """Return a string expression that can be eval()'d when operator names
        are available in the eval globals (we don't prefix with 'np.')."""
        if self.value is None:
            return "None"
        if self.node_type == 'constant':
            # use repr to produce a valid numeric literal
            return repr(float(self.value))
        if self.node_type == 'variable':
            # value is e.g. 'x0' -> produce x[0] (x will be the array passed to lambda)
            if isinstance(self.value, str) and self.value.startswith('x'):
                return f"x[{self.value[1:]}]"
            return str(self.value)
        if self.node_type == 'unary_op':
            operand = self.left.to_string() if self.left is not None else (self.right.to_string() if self.right is not None else "")
            return f"{self.value.__name__}({operand})"
        if self.node_type == 'binary_op':
            left_s = self.left.to_string() if self.left is not None else ""
            right_s = self.right.to_string() if self.right is not None else ""
            return f"{self.value.__name__}({left_s}, {right_s})"
        return ""

