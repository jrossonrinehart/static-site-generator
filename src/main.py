from textnode import TextNode
from htmlnode import HTMLNode

def main():
    testNode = TextNode("This is a text node", "bold", "https://okay.ai")
    print(testNode)
    testHTMLNode = HTMLNode("h1","test value",None,{'href':'test'})
    print(testHTMLNode)

main()
