class HTMLNode():
    def __init__(self, tag=None,value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")

    def props_to_html(self):
        return_string = ""
        if self.props == None:
            return ""
        else:
            for prop in self.props:
                return_string += f" {prop}={self.props[prop]}"
        return return_string

    def __repr__(self):
        text = f"tag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props}"
        return text

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node must have a value")
        elif self.tag == None:
            return self.value
        else:
            props_string = self.props_to_html()
            html_string = f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
            return html_string

class ParentNode(HTMLNode):
    def __init__(self, tag, children,props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag cannot be null")
        if self.children == None or len(self.children) == 0:
            raise ValueError("ParentNode must have children")
        else:
            props_string = self.props_to_html()
            child_string = ""
            for child in self.children:
                child_string += child.to_html()

            return f"<{self.tag}{props_string}>{child_string}</{self.tag}>"


