# // Complete the  function in the editor below, which has 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

def preOrder(root):
    if root == None:
        return

    # // Deal with the node
    print(root.data);

    # // Recur on left subtree
    preOrder(root.left);

    # // Recur on right subtree
    preOrder(root.right);