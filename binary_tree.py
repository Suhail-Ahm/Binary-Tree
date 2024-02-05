class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            return Node(data)
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def delete(self, data):
        # check if root is empty
        if self.data is None:
            return "No data found!"

        # check if data is in left or right
        if data < self.data:
            # in left
            self.left = self.left.delete(data)

        elif data > self.data:
            # right
            self.right = self.right.delete(data)

        else:
            # Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            self.data = self.get_min(self.right)

            self.right = self.right.delete(self.data)

        return self

    def get_min(self, node):
        if node.left is None:
            return node.data
        return self.get_min(node.left)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        print(self.data)

        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.data)

        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):

        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()

        print(self.data)


root = Node(10)
root.insert(7)
root.insert(8)
root.insert(4)
root.insert(11)
root.insert(12)
root.insert(5)
root.insert(9)
# root.preorder_traversal()
# root.delete(7)


#! Problem 1: Find the maximum Depth or Height of given Binary Tree
def get_max_depth_or_height(node):
    if node is None:
        return 0

    left_height = get_max_depth_or_height(node.left)
    # print(f"Left: {left_height}")
    right_height = get_max_depth_or_height(node.right)
    # print(f"Right: {right_height}")

    return max(left_height, right_height) + 1


print(f"max height: {get_max_depth_or_height(root)}")

#! Problem 2: To determine if two trees are identical
a = Node(6)
a.insert(3)
a.insert(9)

b = Node(6)
b.insert(3)
b.insert(9)


def identical_trees(a, b):
    if a is None and b is None:
        return True

    elif a is not None and b is not None:
        left_identical = identical_trees(a.left, b.left)
        right_identical = identical_trees(a.right, b.right)
        return left_identical and right_identical

    return False


print(f"Identical: {identical_trees(a, b)}")
