class Node:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Checking if 2 trees are equal
    def is_same(self, n1 : Node, n2: Node) -> bool:
        if n1 == None or n2 == None:
            return True
        print('n1.val: ', n1.val, 'n2.val: ', n2.val)
        # Condition to check
        # Values should be same and left and right 
        # nodes should be with same values
        if n1.val == n2.val and self.is_same(n1.left, n2.left) and self.is_same(n1.right, n2.right):
            return True
        return False

# if __file__ == '__main__':
n1_left = Node(1,None,None)
n1_right = Node(2,None,None)
n1 = Node(4,n1_left,n1_right)

n2_left = Node(1,None,None)
n2_right = Node(2,None,None)
n2 = Node(4,n2_left,n2_right)

s1 = Solution()
print(s1.is_same(n1,n2))