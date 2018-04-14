from __future__ import print_function

#definition of the tree node

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	# @param {TreeNode} root
	# @return {string[]}
	def binaryTreePath(self, root):
		res = []
		if not root:
			return res
		if not root.left and not root.right:
			res.append(str(root.val))
			return res
		for path in self.binaryTreePath(root.left):
			print("the res is now:", res)
			res.append(str(root.val) + '>' + path)
		for path in self.binaryTreePath(root.right):
			print("the res is now:", res)
			res.append(str(root.val) + '>' + path)

		return res


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
solution = Solution()
print (solution.binaryTreePath(tree))

