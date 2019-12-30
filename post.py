# Imports
from htmlparser import *


# Post class
class Post:
    """
    Holds a single post data
    """

    def __init__(self, num_id, str_content, str_title, str_excerpt, str_name, str_guid):
        # Here be all class vars
        self.id = num_id
        self.content = str_content
        self.title = str_title
        self.excerpt = str_excerpt
        self.name = str_name
        self.link = str_guid

        # Strip unneeded html tags from post content
        html_remover = MyHTMLParser()
        html_remover.feed(self.content)
        self.content = " ".join(html_remover.html_text)

        # Strip remaining non HTML tags (such as [h5p id="#"])
