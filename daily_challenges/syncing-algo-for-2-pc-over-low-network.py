"""
    src: https://gist.github.com/saurabhgokhale/0161185ee6f454fb8a4238dd9bf43dc6
    Implement a file syncing algorithm for two computers over a low-bandwidth network.
    What if we know the files in the two computers are mostly the same?
    Idea: Idea is to use Markle tree for a fixed size data blocks. If the data block
    changes, we identify only the node that needs to be updated by comparing
    CRC32 hash value of the nodes.
"""

import zlib

class Node:
    def __init__(self, data=None):
        self.left = self.right = None
        self.data = data

class MarkleTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def buildTree(self, q):
        while len(q) > 1:
            size_q = len(q)

            for i in range(size_q):
                left_node = q.pop(0)
                i += 1

                right_node = None
                if i < size_q:
                    right_node = q.pop(0)
                    i += 1

                parent_data = left_node.data + (right_node.data if right_node != None else '')
                parent_data_bin = parent_data.encode('utf-8')

                parent_node = Node()
                parent_node.left, parent_node.right = left_node, right_node
                parent_node.data = str(zlib.crc32(parent_data_bin))

                q.append(parent_node)
                
        self.root = q.pop(0)

    def detectChanges(self, current_root, new_root):
        if current_root == new_root == None: 
            return False
        elif current_root == None or new_root == None:
            print("Change detected. Change: data added/deleted")
            return True
        
        left_changes = self.detectChanges(current_root.left, new_root.left)
        right_changes = self.detectChanges(current_root.right, new_root.right)

        if current_root.data != new_root.data:
            print("Change in the data detected. RootHash of the changes: " + new_root.data)
            return True
        
        return left_changes or right_changes
    
    def mergeChange(self, current_root, new_root):
        if current_root == new_root == None:
            return None
        elif new_root == None:
            print("Change detected. Change: data deleted")
            return None
        elif current_root == None:
            print("Change detected. Change: data added")
            return None
        elif current_root.data != new_root.data:
            current_root.data = new_root.data

        current_root.left = self.mergeChange(current_root.left, new_root.left)
        current_root.right = self.mergeChange(current_root.right, new_root.right)

        return current_root

if __name__ == '__main__':
    getListNode = lambda l: [Node(i) for i in l]
        
    list_A = getListNode(['A', 'B', 'C', 'D', 'E'])
    tree_A = MarkleTree()
    tree_A.buildTree(list_A)
    print(f'Root Hash of current tree: {tree_A.root.data}')

    list_B = getListNode(['AA', 'B', 'C', 'D', 'E'])
    tree_B = MarkleTree()
    tree_B.buildTree(list_B)
    print(f'Root Hash of current tree: {tree_B.root.data}')

    if(tree_A.detectChanges(tree_A.root, tree_B.root)):
        tree_A.root = tree_A.mergeChange(tree_A.root, tree_B.root)