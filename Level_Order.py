class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def level_order(root):
        curr = root
        q= []

        while curr:
            if curr.left and curr.right:
                q.append(curr.left)
                q.append(curr.right)
            elif curr.left and not curr.right:
                q.append(curr.left)
            elif curr.right and not curr.left:
                q.append(curr.right)
            print(curr.data, end = " ")
            if len(q) != 0:
                curr = q.pop(0)
            else:
                break
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.left.right = Node(5)

Node.level_order(root)