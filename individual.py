import numpy as np
import random
import matplotlib.pyplot as plt
from node import Node
from protectedOperators import unary_ops, binary_ops

CONSTANT = [
    np.pi,
    np.e,
    np.sqrt(2),
    np.sqrt(3),
    random.uniform(-10.0, -1.0),
    random.uniform(1.0, 10.0),
]

class Tree:
    def __init__(self, max_depth, x_train, y_train, tree_attempts=10):
        self.root = None
        self.max_depth = max_depth
        self.fitness = None
        self.x_train = x_train
        self.y_train = y_train
        self.var_num = x_train.shape[0]
        self.vars = [f'x{i}' for i in range(self.var_num)]
        self.tree_attempts = tree_attempts

    def populate(self):
        self.root = self.generate_random_tree()
        self.compute_fitness()

    def generate_random_tree(self, current_depth=0, max_depth=None):
        if max_depth is None:
            max_depth = self.max_depth

        x_mean = np.mean(self.x_train)
        x_std = np.std(self.x_train)
        if x_std < 1e-6:
            const_min, const_max = x_mean - 1, x_mean + 1
        else:
            const_min, const_max = x_mean - 2 * x_std, x_mean + 2 * x_std

        if current_depth >= max_depth:
            if random.random() < 0.5:
                return Node('variable', self.vars[random.randint(0, self.var_num - 1)])
            else:
                return Node('constant', CONSTANT[random.randint(0, len(CONSTANT) - 1)])
        else:
            if random.random() < 0.7:
                if random.random() < 0.5:
                    op = random.choice(binary_ops)
                    left = self.generate_random_tree(current_depth + 1, max_depth)
                    right = self.generate_random_tree(current_depth + 1, max_depth)
                    return Node('binary_op', op, left, right)
                else:
                    op = random.choice(unary_ops)
                    child = self.generate_random_tree(current_depth + 1, max_depth)
                    return Node('unary_op', op, child, None)
            else:
                if random.random() < 0.5:
                    return Node('variable', self.vars[random.randint(0, self.var_num - 1)])
                else:
                    return Node('constant', CONSTANT[random.randint(0, len(CONSTANT) - 1)])

    def compute_fitness(self, get_pred=False):
        """
        Convert tree to string and eval it after injecting all available operators
        (both numpy and protected ones) into the eval namespace.
        """
        expression = self.root.to_string()
        # base globals: numpy for protected wrappers that internally call np
        eval_globals = {"np": np, "nan": np.nan, "inf": np.inf}

        # Inject every operator function (use its __name__ as identifier)
        for op in (unary_ops + binary_ops):
            eval_globals[op.__name__] = op

        try:
            formula = eval(f"lambda x: {expression}", eval_globals)
            y_pred = formula(self.x_train)

            # Guard against bad outputs
            if np.isnan(y_pred).any() or np.isinf(y_pred).any():
                raise ValueError("y_pred contains NaN or Inf")

            self.fitness = float(np.mean((self.y_train - y_pred) ** 2))

            if get_pred:
                return y_pred
        except Exception as e:
            # Helpful debug output: show expression and what names were available.
            # Remove or reduce prints once you debugged the problem.
            #print("ERROR evaluating tree expression:", e)
            #print("Expression:", expression)
            #print("Available names in eval globals (sample):", sorted(list(eval_globals.keys()))[:40])
            # Set fitness to infinity so GP treats this individual as invalid
            self.fitness = np.inf

    # --- cloning, traversal, mutation & recombination follow (unchanged logic from your original) ---

    def clone_tree(self):
        new_tree = Tree(max_depth=self.max_depth, x_train=self.x_train, y_train=self.y_train, tree_attempts=self.tree_attempts)
        new_tree.root = self.root.clone_node() if self.root is not None else None
        new_tree.fitness = self.fitness
        return new_tree

    def get_all_nodes(self, node=None, parent=None, is_left=None, depth=0):
        if node is None:
            node = self.root
        nodes = [(node, parent, is_left, depth)]
        if node.left is not None:
            nodes.extend(self.get_all_nodes(node.left, node, True, depth + 1))
        if node.right is not None:
            nodes.extend(self.get_all_nodes(node.right, node, False, depth + 1))
        return nodes

    def _get_subtree_height(self, node):
        if node is None:
            return 0
        left_h = self._get_subtree_height(node.left) if node.left is not None else 0
        right_h = self._get_subtree_height(node.right) if node.right is not None else 0
        return 1 + max(left_h, right_h)

    def mutate(self):
        """Perform mutation on the tree."""
        if random.random() < 0.6:
            self.mutate_subtree()
        else:
            mutate_choice = random.choice([0, 1, 2, 3])
            if mutate_choice == 0:
                self.mutate_point()
            elif mutate_choice == 1:
                self.mutate_permutation()
            elif mutate_choice == 2:
                self.mutate_hoist()
            else:
                self.mutate_collapse()

    def mutate_subtree(self):
        """
        Perform mutation by selecting a random node in the tree and replacing it
        with a new randomly generated subtree that does not cause the overall
        tree depth to exceed the allowed maximum. Keep creating a new subtree
        until the fitness is valid.
        """
        nodes = self.get_all_nodes()  # Each tuple is (node, parent, is_left, depth)
        attempts = self.tree_attempts
        valid_subtree_found = False
        
        while attempts > 0 and not valid_subtree_found:
            node_to_mutate, parent, is_left, node_depth = random.choice(nodes)
            
            # Calculate remaining depth allowed for the new subtree.
            remaining_depth = self.max_depth - node_depth
            
            # Generate a new subtree with maximum allowed height equal to the remaining depth.
            new_subtree = self.generate_random_tree(current_depth=0, max_depth=remaining_depth)
            
            # Temporarily replace the selected node (or the entire tree if it is the root).
            if parent is None:
                self.root = new_subtree
            else:
                if is_left:
                    parent.left = new_subtree
                else:
                    parent.right = new_subtree
            
            # Compute fitness and check if it is valid.
            self.compute_fitness()
            if self.fitness != np.inf:
                valid_subtree_found = True
            else:
                # Revert the change if the fitness is not valid.
                if parent is None:
                    self.root = node_to_mutate
                else:
                    if is_left:
                        parent.left = node_to_mutate
                    else:
                        parent.right = node_to_mutate
            
            attempts -= 1

    def mutate_point(self):
        """Performs a point mutation by changing a randomly selected node."""
        nodes = self.get_all_nodes()
        if not nodes:
            return
        node, _, _, _ = random.choice(nodes)
        
        if node.node_type == 'binary_op':
            node.value = random.choice(binary_ops)
        elif node.node_type == 'unary_op':
            node.value = random.choice(unary_ops)
        
        self.compute_fitness()
    
    def mutate_permutation(self):
        """Swaps the left and right child of a randomly chosen binary operator."""
        binary_nodes = [n for n in self.get_all_nodes() if n[0].node_type == 'binary_op']
        if not binary_nodes:
            return
        node, _, _, _ = random.choice(binary_nodes)
        node.left, node.right = node.right, node.left
        self.compute_fitness()
    
    def mutate_hoist(self):
        """Replaces a randomly selected subtree with one of its sub-subtrees."""
        nodes = self.get_all_nodes()
        attempts = self.tree_attempts
        if not nodes:
            return
        
        node, _, _, _ = random.choice(nodes)
        while attempts > 0 and node.left is None and node.right is None:
            attempts -= 1
            node, _, _, _ = random.choice(nodes)
            
        if attempts <= 0:
            return
        self.root = node
        self.compute_fitness()
    
    def mutate_collapse(self):
        """Replaces a randomly selected subtree with a constant equal to its evaluated mean value."""
        nodes = self.get_all_nodes()
        if not nodes:
            return

        attempts = self.tree_attempts
        valid_collapse_found = False

        while attempts > 0 and not valid_collapse_found:
            node, parent, is_left, _ = random.choice(nodes)

            if node.node_type not in ['binary_op', 'unary_op']:
                attempts -= 1
                continue  # Skip if it's not a valid operator node

            try:
                expression = node.to_string()
                eval_globals = {"np": np, "nan": np.nan, "inf": np.inf}

                formula = eval(f"lambda x: {expression}", eval_globals)
                collapsed_value = float(np.mean(formula(self.x_train)))
            except:
                collapsed_value = 0.0

            new_node = Node('constant', collapsed_value)
            if parent is None:
                self.root = new_node
            else:
                if is_left:
                    parent.left = new_node
                else:
                    parent.right = new_node

            self.compute_fitness()

            if self.fitness != np.inf:
                valid_collapse_found = True
            else:
                # Revert the change if fitness is invalid
                if parent is None:
                    self.root = node
                else:
                    if is_left:
                        parent.left = node
                    else:
                        parent.right = node

            attempts -= 1

    def recombine(self, other_tree):
        """
        Perform recombine with another tree by swapping randomly chosen subtrees.
        The swap is only accepted if it does not cause the overall depth of either
        offspring to exceed the maximum allowed depth and the fitness is valid.
        
        Parameters:
            other_tree: The other tree to recombine with.
        
        Returns:
            tuple: Two new offspring trees.
        """
        offspring1 = self.clone_tree()
        offspring2 = other_tree.clone_tree()
        
        nodes1 = offspring1.get_all_nodes()  # (node, parent, is_left, depth)
        nodes2 = offspring2.get_all_nodes()
        
        attempts = self.tree_attempts
        valid_swap_found = False
        
        while attempts > 0 and not valid_swap_found:
            node1, parent1, is_left1, depth1 = random.choice(nodes1)
            node2, parent2, is_left2, depth2 = random.choice(nodes2)
            
            height1 = offspring1._get_subtree_height(node1)
            height2 = offspring2._get_subtree_height(node2)
            
            # Check: after swapping, the new depth in offspring1 would be:
            #   depth1 (depth of the replacing location) + height2 (height of subtree from tree2)
            # Similarly for offspring2.
            if (depth1 + height2 <= self.max_depth) and (depth2 + height1 <= self.max_depth):
                # Clone the chosen subtrees.
                subtree1 = node1.clone_node()
                subtree2 = node2.clone_node()
                
                # Swap subtree in offspring1.
                if parent1 is None:
                    offspring1.root = subtree2
                else:
                    if is_left1:
                        parent1.left = subtree2
                    else:
                        parent1.right = subtree2
                        
                # Swap subtree in offspring2.
                if parent2 is None:
                    offspring2.root = subtree1
                else:
                    if is_left2:
                        parent2.left = subtree1
                    else:
                        parent2.right = subtree1

                # Compute fitness and check if it is valid.
                offspring1.compute_fitness()
                offspring2.compute_fitness()
                
                if offspring1.fitness != np.inf and offspring2.fitness != np.inf:
                    valid_swap_found = True
                    break
                else:
                    # Revert the change if the fitness is not valid.
                    if parent1 is None:
                        offspring1.root = node1
                    else:
                        if is_left1:
                            parent1.left = node1
                        else:
                            parent1.right = node1
                            
                    if parent2 is None:
                        offspring2.root = node2
                    else:
                        if is_left2:
                            parent2.left = node2
                        else:
                            parent2.right = node2

            attempts -= 1
        
        # If no valid swap was found, return the unchanged offspring.
        if not valid_swap_found:
            return self.clone_tree(), other_tree.clone_tree()
        
        return offspring1, offspring2

    def plot(self):
        """Plot the tree. If a node has only one child, the line to that child is drawn vertically.
        The vertical gap between parent and child is minimized by drawing the line from center to center."""
        def draw_node(node, x, y, dx, dy):
            if node is not None:
                bbox = None
                fontsize = 11
                if node.node_type in ["binary_op", "unary_op"]:
                    text = node.value.__name__
                    fontsize += 1
                    bbox = dict(facecolor='white', edgecolor='none')
                elif node.node_type == "variable":
                    text = node.to_string()
                    bbox = dict(boxstyle='circle', edgecolor='black', facecolor='tomato')
                elif node.node_type == "constant":
                    text = str(round(float(node.to_string()), 2))
                    bbox = dict(boxstyle='circle', edgecolor='black', facecolor='lightgreen')
                else:
                    text = ""
                
                plt.text(x, y, text, ha='center', va='center', fontsize=fontsize, bbox=bbox)
                
                if node.left is not None and node.right is not None:
                    plt.plot([x, x - dx], [y, y - dy], color='black')
                    draw_node(node.left, x - dx, y - dy, dx / 2, dy)
                    plt.plot([x, x + dx], [y, y - dy], color='black')
                    draw_node(node.right, x + dx, y - dy, dx / 2, dy)
                elif node.left is not None:
                    plt.plot([x, x], [y, y - dy], color='black')
                    draw_node(node.left, x, y - dy, dx / 2, dy)
                elif node.right is not None:
                    plt.plot([x, x], [y, y - dy], color='black')
                    draw_node(node.right, x, y - dy, dx / 2, dy)

        plt.figure(figsize=(15, 10))
        plt.axis('off')
        plt.title("Tree Structure", fontsize=14)
        draw_node(self.root, 0, 0, 20, 1)
        plt.show()

    def __str__(self):
        """
        Return the string representation of the tree (its formula).
        
        Returns:
            str: The string representation of the tree's formula.
        """
        return self.root.to_string() if self.root is not None else ""
