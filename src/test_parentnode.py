import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        html_string = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), html_string)

    def test_parent_in_parent_to_html(self):
        node = ParentNode(
        "p",
        [
            ParentNode("b",
                       [ 
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                        ]),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        html_string = "<p><b>Normal text<i>italic text</i>Normal text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), html_string)
    
    def test_to_html_no_children(self):
        node = ParentNode(
        "p",
        [],
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception),"ParentNode must have children")
    def test_to_html_no_children(self):
        node = ParentNode(
        "p",
        [LeafNode(None, "Normal text")],
        )
        node.children = None
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception),"ParentNode must have children")
    
    def test_one_child_to_html(self):
        node = ParentNode(
        "p",
        [LeafNode(None, "Normal text")],
        )
        self.assertEqual(node.to_html(), "<p>Normal text</p>")