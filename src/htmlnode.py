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
            return None
        else:
            for prop in props:
                return_string += f" {prop}={props[prop]}"
        return return_string

    def __repr__(self):
        text = f"tag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props}"
        return text
