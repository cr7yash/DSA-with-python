import unittest
import sys
from io import StringIO
from BinaryTree_Linked_list import TreeNode, preorderTraversal, inorderTraversal, postorderTraversal, levelorderTraversal, searchBT, insertNodeBT

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        """Set up a new tree for each test."""
        self.root = TreeNode("Drinks")
        self.hot = TreeNode("Hot")
        self.cold = TreeNode("Cold")
        self.tea = TreeNode("Tea")
        self.coffee = TreeNode("Coffee")
        self.coke = TreeNode("Coke")

        self.root.leftChild = self.hot
        self.root.rightChild = self.cold
        self.hot.leftChild = self.tea
        self.hot.rightChild = self.coffee
        self.cold.leftChild = self.coke

        # For capturing print output
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """Restore stdout."""
        sys.stdout = self.held

    def test_treenode_creation(self):
        node = TreeNode("Test")
        self.assertEqual(node.data, "Test")
        self.assertIsNone(node.leftChild)
        self.assertIsNone(node.rightChild)

    def test_preorder_traversal(self):
        preorderTraversal(self.root)
        expected_output = "Drinks\nHot\nTea\nCoffee\nCold\nCoke\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_preorder_traversal_empty(self):
        preorderTraversal(None)
        self.assertEqual(sys.stdout.getvalue(), "")

    def test_inorder_traversal(self):
        inorderTraversal(self.root)
        expected_output = "Tea\nHot\nCoffee\nDrinks\nCoke\nCold\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_inorder_traversal_empty(self):
        inorderTraversal(None)
        self.assertEqual(sys.stdout.getvalue(), "")

    def test_postorder_traversal(self):
        postorderTraversal(self.root)
        expected_output = "Tea\nCoffee\nHot\nCoke\nCold\nDrinks\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_postorder_traversal_empty(self):
        postorderTraversal(None)
        self.assertEqual(sys.stdout.getvalue(), "")

    def test_levelorder_traversal(self):
        levelorderTraversal(self.root)
        expected_output = "Drinks\nHot\nCold\nTea\nCoffee\nCoke\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_levelorder_traversal_empty(self):
        levelorderTraversal(None)
        self.assertEqual(sys.stdout.getvalue(), "")

    def test_search_bt_success(self):
        self.assertEqual(searchBT(self.root, "Coke"), "Success")
        self.assertEqual(searchBT(self.root, "Drinks"), "Success")

    def test_search_bt_not_found(self):
        self.assertEqual(searchBT(self.root, "Pepsi"), "Not found")

    def test_search_bt_empty_tree(self):
        self.assertEqual(searchBT(None, "Coke"), "Not found")

    def test_insert_node_bt(self):
        new_node = TreeNode("Fanta")
        result = insertNodeBT(self.root, new_node)
        self.assertEqual(result, "Successful insert")
        self.assertIsNotNone(self.cold.rightChild)
        self.assertEqual(self.cold.rightChild.data, "Fanta")

    def test_insert_node_bt_fill_gap(self):
        # Create a tree with a missing left child
        root = TreeNode("A")
        root.rightChild = TreeNode("C")
        new_node = TreeNode("B")
        
        result = insertNodeBT(root, new_node)
        self.assertEqual(result, "Successful insert")
        self.assertIsNotNone(root.leftChild)
        self.assertEqual(root.leftChild.data, "B")

    def test_insert_node_bt_empty_tree(self):
        root = None
        new_node = TreeNode("First")
        # The function as written doesn't modify the root if it's None,
        # but we can test the return value.
        # A better implementation would handle this case by returning the new node.
        result = insertNodeBT(root, new_node)
        self.assertEqual(result, "Successful insert")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)