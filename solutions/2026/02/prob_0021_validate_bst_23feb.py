class Solution:
    def validateBST(self, root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')):
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        return (self.validateBST(root.left, min_val, root.val) and
                self.validateBST(root.right, root.val, max_val))

# --- Test Cases ---
if __name__ == '__main__':
    # Create a binary search tree
    #       4
    #      / \
    #     2   6
    #    / \   \
    #   1   3   7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.validateBST(root))  # Expected: True

    # Create an invalid binary search tree
    #       4
    #      / \
    #     2   6
    #    / \   \
    #   1   3   7
    #    / \
    #   0   8
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(0)
    root.left.left.right = TreeNode(8)

    print(s.validateBST(root))  # Expected: False