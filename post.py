# Imports
from htmlparser import *
from re import sub
import foreign


# Post class
class Post:
    """
    Holds a single post data
    """

    def __init__(self, num_id, str_content, str_title, str_excerpt, str_name, str_guid):
        # Here be all class vars
        self.id = num_id  # ID
        self.content = list()  # Post content
        self.title = str_title  # Post title
        self.excerpt = str_excerpt  # Post excerpt
        self.name = str_name  # Post name
        self.link = str_guid  # Post link
        self.content_small_list = list()
        self.content_complete_list = list()

        # Strip unneeded html tags from post content
        html_remover = MyHTMLParser()
        html_remover.feed(str_content)

        # Strip remaining non HTML tags (such as [h5p id="#"])
        for item in html_remover.html_text:
            temp = sub(r" ?\[[^)]+\]", "****h5p_item****", item)
            self.content.append(temp)

        html_remover.close()

        words = list()

        # Mark foreign words
        for post_text in self.content:
            words += foreign.word_breaker(post_text)
        self.content_complete_list, self.content_small_list = foreign.lang_marker(words, "‡‡‡‡ ", " ‡‡‡‡", "he")
