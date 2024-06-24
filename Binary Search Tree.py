#1. Binary Search Tree
class BST:
    class _Node:
        def __init__(self,ele):
            self.data = ele
            self.left = None
            self.right = None
        def __init__(self):
            self.root = None
            self.count = 0
        def isEmpty(self):
            return self.count == 0
        def getNodeCount(self):
            return self.count
#adding node into BST        
        def addNode(self,ele):
            cur = parent = self.root
            while cur!= None and cur.data!= ele:
                parent = cur
                if ele>cur.data:
                    cur = cur.left
                else:
                    cur = cur.right
                if cur == None:
                    new_node = self._Node(ele)
                if parent == None:
                    self.root = new_node
                elif ele<parent.data:
                    parent.left = new_node
                elif ele> parent.data:
                        parent.right = new_node
                        self.count+= 1

#2. Inorder
def inorder(self):
    if not self.isEmpty():
        self._inorder_(self.root)
def _inorder_(self,node):
    if node!= None:
        self._inorder_(node.left)
        print(node.data)
        self._inorder_(node.right)

#preorder
def preorder(self):
    if not self.isEmpty():
        self._preorder_(self.root)
def _preorder_(self,root):
    if node!= None:
        print(node,data)
        self._preorder_(node,left)
        self._preorder_(node,right)

#postorder
def postorder(self):
    if not self.isEmpty():
        self_postorder_(self.root)
def _postorder_(self,node):
    if node!= None:
        self._postorder_(node.left)
        self._postorder_(node.right)
        print(node.data)

#levelorder
def levelorder(self):
    if not self.isEmpty():
        self_postorder_(self.root)
        queue = []
        result = []
        queue.append(root)
    while queue:
        cur_node = queue.pop(0)
        result.append(cur_node.data)
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return result

#3. Write method to find the height of BST
def getDepthOfTree(self):
    if not self.isEmpty():
        return(self._depthOfTree_(self.root))
    if root is None:
        return -1  
    left_depth = getDepthOfTree(self.left)
    right_depth = getDepthOfTree(self.right)
    return max(left_depth, right_depth) + 1

#4. write method to count number of terminal nodes
def terminalNodeCount(self):
    if not self.isEmpty():
        return self.terminalNodeCount_recurcive(self.root)

    def terminalNodeCount_recurcive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        left_count = self.terminalNodeCount_recurcive(node.left)
        right_count = self.terminalNodeCount_recurcive(node.right)
        return left_count + right_count

#5. Write method to delete specified node from BST
def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

def _delete_recursive(self, root, data):
    if root is None:
            return root
    if data < root.data:
            root.left = self._delete_recursive(root.left, data)
    elif data > root.data:
            root.right = self._delete_recursive(root.right, data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
            root.data = self._get_min_value(root.right)
            root.right = self._delete_recursive(root.right, root.data)
            return root
def _get_min_value(self, node):
    while node.left is not None:
        node = node.left
    return node.data

def inorder_traversal(self, node):
    if node is not None:
        self.inorder_traversal(node.left)
        print(node.data, end=' ')
        self.inorder_traversal(node.right)

#6. Write method to traverse the BST in descending order
def reverse_inorder_traversal(self):
        return self._reverse_inorder_recursive(self.root)
def _reverse_inorder_recursive(self, node):
    if node is not None:
        right = self._reverse_inorder_recursive(node.right)
        print(node.data, end=' ')
        left = self._reverse_inorder_recursive(node.left)
        return right, node, left
    else:
        return None, None, None
    
