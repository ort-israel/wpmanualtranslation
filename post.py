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
        self.id = num_id
        self.content = list()
        self.title = str_title
        self.excerpt = str_excerpt
        self.name = str_name
        self.link = str_guid
        self.small_list = list()
        self.complete_list = list()

        # Strip unneeded html tags from post content
        html_remover = MyHTMLParser()
        html_remover.feed(str_content)

        # Strip remaining non HTML tags (such as [h5p id="#"])
        with html_remover.html_text as item:
            temp = sub(r" ?\[[^)]+\]", "****h5p item ****", item)
            self.content.append(temp)

        # Put the result in self.content and close the parser
        # self.content = " ".join(segments_list)
        # I think that a list of string is better as it's my only way to separate the content into segments.
        html_remover.close()

        # Mark foreign words
        with self.content as post_text:
            words = foreign.word_breaker(post_text)
        self.complete_list, self.small_list = foreign.lang_marker(words, "‡‡‡‡", "", "he")
