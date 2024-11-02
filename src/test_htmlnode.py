import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    #testing that props_to_html returns None when props is not given
    def test_no_props(self):
        testHTMLNode = HTMLNode("h1","test value")
        self.assertEqual(testHTMLNode.props_to_html(), "")
    
    #testing props_to_html
    def test_props_to_html(self):
        props = {
            'href':'/test/cool',
            'target': '_blank'
        }
        return_string = " href=/test/cool target=_blank"
        TestHTMLNode = HTMLNode("h1", "test value",None,props=props)
        self.assertEqual(TestHTMLNode.props_to_html(),return_string)
        

        






