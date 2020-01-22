# Imports
from htmlparser import *
from re import sub
import foreign


# Post class
class Post:
    """
    Holds a single post, page or media data
    """

    def __init__(self, num_id: str, str_content: str, str_title: str, str_excerpt: str, str_name: str, str_guid: str,
                 str_mark_start: str, str_mark_end: str):
        # Here be all class vars
        self.id = num_id  # ID
        self.content = list()  # Post content
        self.title = str_title  # Post title
        self.excerpt = str_excerpt  # Post excerpt
        self.name = str_name  # Post name
        self.link = str_guid  # Post link
        self.content_small_list = list()
        self.content_complete_list = list()
        self.excerpt_small_list = list()
        self.excerpt_complete_list = list()

        # Strip unneeded html tags from post content
        html_remover = MyHTMLParser()
        html_remover.feed(str_content)

        # Strip remaining non HTML tags (such as [h5p id="#"])
        for item in html_remover.html_text:
            temp = sub(r" ?\[[^)]+\]", "****h5p_item****", item)
            self.content.append(temp)

        html_remover.close()

        words = list()

        # Mark foreign words in content
        for post_text in self.content:
            words += foreign.word_breaker(post_text)
        self.content_complete_list, self.content_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, "he")

        words = foreign.word_breaker(self.excerpt)

        # Mark foreign words in excerpt
        self.excerpt_complete_list, self.excerpt_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, "he")
