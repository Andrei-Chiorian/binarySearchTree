
class TreeNode:
    # TreeNode is a class for representing a node in a binary search tree.
    #
    # The following fields are supported:
    #
    # - `key`: the value stored in the node
    # - `left`: the left subtree of the node
    # - `right`: the right subtree of the node
    #
    # The `__init__` method is the constructor for the TreeNode class. It takes a
    # single argument `key` and creates a new TreeNode with the specified key.
    #
    # The `__str__` method is used to create a string representation of the node.
    # Currently, it simply returns the string representation of the key.

    def __init__(self, key):
        # The `key` field stores the value stored in the node.
        self.key = key
        # The `left` field stores the left subtree of the node.
        self.left = None
        # The `right` field stores the right subtree of the node.
        self.right = None

    def __str__(self):
        # The `__str__` method is used to create a string representation of the
        # node. Currently, it simply returns the string representation of the
        # key.
        return str(self.key)


class BinarySearchTree:
    """
    BinarySearchTree is a class for representing a binary search tree.

    The following methods are supported:

    - `insert(key)`: inserts the key into the tree
    - `search(key)`: searches for the key in the tree
    - `delete(key)`: deletes the key from the tree
    - `inorder_traversal()`: returns the inorder traversal of the tree
    """

    def __init__(self):
        # The `root` field is used to store the root node of the tree.
        self.root = None

    def _insert(self, node, key):
        # If the node is `None`, the key isn't in the tree, so we return a new
        # `TreeNode` with the key.
        if node is None:
            return TreeNode(key)

        # If the key is less than the node's key, we need to insert it in the
        # left subtree.
        if key < node.key:
            # We recursively call `_insert` on the left subtree.
            node.left = self._insert(node.left, key)
        # If the key is greater than the node's key, we need to insert it in the
        # right subtree.
        elif key > node.key:
            # We recursively call `_insert` on the right subtree.
            node.right = self._insert(node.right, key)
        # If the key is equal to the node's key, we don't need to do anything.
        # Returning the node as is.
        return node

    def insert(self, key):
        # Insert the key into the tree. This is a wrapper for the `_insert`
        # method.
        self.root = self._insert(self.root, key)

    def _search(self, node, key):
        # If the node is `None` or the node's key is equal to the key, we
        # return the node.
        if node is None or node.key == key:
            return node
        # If the key is less than the node's key, we need to search in the left
        # subtree.
        if key < node.key:
            # We recursively call `_search` on the left subtree.
            return self._search(node.left, key)
        # If the key is greater than the node's key, we need to search in the
        # right subtree.
        return self._search(node.right, key)

    def search(self, key):
        # Search for the key in the tree. This is a wrapper for the `_search`
        # method.
        return self._search(self.root, key)

    def _delete(self, node, key):
        # If the node is `None`, the key isn't in the tree, so we simply return
        # the node as is.
        if node is None:
            return node
        # If the key is less than the node's key, we need to delete it in the
        # left subtree.
        if key < node.key:
            # We recursively call `_delete` on the left subtree.
            node.left = self._delete(node.left, key)
        # If the key is greater than the node's key, we need to delete it in the
        # right subtree.
        elif key > node.key:
            # We recursively call `_delete` on the right subtree.
            node.right = self._delete(node.right, key)
        # If the key is equal to the node's key, we need to delete the node.
        else:
            # If the node has no left subtree, we can replace it with its right
            # subtree.
            if node.left is None:
                return node.right
            # If the node has no right subtree, we can replace it with its left
            # subtree.
            elif node.right is None:
                return node.left
            # If the node has both left and right subtrees, we need to find the
            # node with the minimum key in the right subtree, copy its key, and
            # then delete it.
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)

        return node

    def delete(self, key):
        # Delete the key from the tree. This is a wrapper for the `_delete`
        # method.
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        # Find the node with the minimum key in the subtree.
        while node.left is not None:
            node = node.left
        # Return the key of the node with the minimum key.
        return node.key

    def _inorder_traversal(self, node, result):
        # If the node is `None`, we can return early.
        if node:
            # Recursively traverse the left subtree.
            self._inorder_traversal(node.left, result)
            # Append the key of the node to the result.
            result.append(node.key)
            # Recursively traverse the right subtree.
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        # Return the inorder traversal of the tree.
        result = []
        self._inorder_traversal(self.root, result)
        return result
