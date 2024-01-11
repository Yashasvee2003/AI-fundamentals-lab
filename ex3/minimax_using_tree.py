class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(arr, i, n):
    root = None
    if i < n:
        root = TreeNode(arr[i])
        root.left = insert(arr, 2 * i + 1, n)
        root.right = insert(arr, 2 * i + 2, n)
    return root


def main():
    root = None
    arr = [1, 3, 4, 7, 8, 9, 10]
    root = insert(arr, 0, len(arr))
    num = minmax(root, 0)
    # print("Max is = ",num)
    # printtree(root)


def minmax(root, level):

    if root.left is not None and root.right is not None:

        # First recur on left child
        left = minmax(root.left, level + 1)

        # Now recur on right child
        right = minmax(root.right, level + 1)

        # Then print the data of node
        if level % 2:
            root.value = min(left, right)
        else:
            root.value = max(left, right)

        print(f"Root value is = {root.value}", end=" ")
        print("The level is = ", level, "----->", level % 2)

        return root.value

    if root.left is None and root.right is None:
        print(f"Root value is = {root.value}", end=" ")
        print("The level is = ", level, "----->", level % 2)
    return root.value


def printtree(node):
    if node == None:
        return

    # First recur on left subtree
    printtree(node.left)

    # Then recur on right subtree
    printtree(node.right)

    # Now deal with the node
    print(node.value, end=" ")


main()
