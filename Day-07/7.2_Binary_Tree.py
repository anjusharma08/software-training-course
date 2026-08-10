# ===============================================================
# Day 07 – Python Binary Tree Practice
# ===============================================================

# Topics:
# 1. Tree Node
# 2. Creating Tree Nodes
# 3. Adding Child Nodes
# 4. Displaying Tree Structure

# ===============================================================
# Q1. Create a Tree and Add Child Nodes
# ===============================================================

class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = [] if children is None else children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


tree = TreeNode('Drink')
cold = TreeNode('Cold')
hot = TreeNode('Hot')

tree.addChild(hot)
tree.addChild(cold)

tea = TreeNode('Tea')
coffee = TreeNode('Coffee')

alcoholic = TreeNode('Alcholic')
non_alcoholic = TreeNode("Non Alchohalic")

cold.addChild(alcoholic)
cold.addChild(non_alcoholic)

# ===============================================================
# End of Day 07 – Binary Tree Practice
# ===============================================================
