# Definition for a binary tree node.
class TreeNode(object):
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def isMirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return(t1.val == t2.val) and isMirror(t1.left , t2.right) and isMirror(t1.right,t2.left)

        if not root:
            return True  
        return isMirror(root.left, root.right)
solution = Solution()
