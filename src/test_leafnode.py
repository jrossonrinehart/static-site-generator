import unittest
from leafnode import LeafNode

from textnode import TextNode, TextType


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_props(self):
        testLeafNode = LeafNode("h1", "test")
        self.assertEqual(testLeafNode.to_html(), "<h1>test</h1>")
    
    def test_to_html_with_props(self):
        props1 = {
            "href": "/google.com",
            "target": "_end"
            }
        testLeafNode = LeafNode("div", "test", props1)
        self.assertEqual(testLeafNode.to_html(),"<div href=/google.com target=_end>test</div>")

    def test_no_value(self):
        testLeafNode = LeafNode("h1", "test")
        testLeafNode.value = None
        with self.assertRaises(ValueError) as context:
            testLeafNode.to_html()
        self.assertEqual(str(context.exception),"leaf node must have a value")

    def test_no_tag(self):
        testLeafNode = LeafNode(None, "test")
        self.assertEqual(testLeafNode.to_html(),"test")
