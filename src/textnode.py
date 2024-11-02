from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode):
        if self.text == TextNode.text and self.text_type == TextNode.text_type and self.url == TextNode.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode("b", text_node.text,)
        case TextType.TEXT:
            return LeafNode(None,text_node.text,)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text,)
        case TextType.CODE:
            return LeafNode("code", text_node.text,)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("Text Type not recognized")


