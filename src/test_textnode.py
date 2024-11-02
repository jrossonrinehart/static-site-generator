import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    def test_text_node_to_html_node(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(),"<b>This is a text node</b>")
    
    def test_text_node_to_html_link(self):
        text_node = TextNode("This is a text node", TextType.LINKS, "/some_image")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(),"<a href=/some_image>This is a text node</a>")

    def test_text_node_to_html_img(self):
        text_node = TextNode("This is a text node", TextType.IMAGES, "/some_image")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(),"<img src=/some_image alt=This is a text node></img>")


if __name__ == "__main__":
    unittest.main()
