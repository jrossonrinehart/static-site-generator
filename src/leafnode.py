from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=None)
        self.props = props
    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node must have a value")
        elif self.tag == None:
            return self.value
        else:
            props_string = self.props_to_html()
            html_string = f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
            return html_string
    