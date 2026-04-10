class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=float('-inf'), upper=float('inf')):
        if not root:
            return True
        val = root.val
        if val <= lower or val >= upper:
            return False
        left = self.isValidBST(root.left, lower, val)
        right = self.isValidBST(root.right, val, upper)
        return left and right

if __name__ == '__main__':
    # Create a binary search tree for testing
    #       2
    #      / \
    #     1   3
    #    /
    #   0
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)

    s = Solution()
    print(s.isValidBST(root))  # Expected: True