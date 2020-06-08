class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorder_t(root):
        curr = root
        s = []
        while curr:
            while curr:
                print(curr.data, end = " ")
                if curr.right and curr.left:
                    s.append(curr)
                    curr = curr.left
                elif curr.right and not curr.left:
                    s.append(curr)
                    break
                elif curr.left and not curr.right:
                    curr = curr.left
                elif not curr.right and not curr.left:
                    curr = None
            if len(s) != 0:
                curr = s.pop()
                curr = curr.right
                print(curr.data, end = " ")
                if curr.left and curr.right:
                    s.append(curr)
                    curr = curr.left
                elif curr.left and not curr.right:
                    curr = curr.left
                elif curr.right and not curr.left:
                    curr = curr.right
                elif (curr.right== None and curr.left == None) and (len(s) != 0):
                    curr = s.pop()
                    curr = curr.right
                else:
                    curr = None


    def postorder_t(root):
        s= []
        curr = root
        while curr:
            if curr.right and curr.left:
                s.append(curr)
                s.append(curr.right)
                curr = curr.left
            elif curr.right and not curr.left:
                s.append(curr)
                curr = curr.right
            elif curr.left and not curr.right:
                s.append(curr)
                curr = curr.left
            elif not curr.right and not curr.left:
                break

        while (curr):
            print(curr.data, end = " ")
            if (len(s) != 0):
                curr = s.pop()
            elif len(s) == 0:
                break
        print('\n')


root = Node(1)
root.left = Node(2)
root.left.right = Node(3)
root.left.right.left = Node(4)



Node.postorder_t(root)
Node.preorder_t(root)
