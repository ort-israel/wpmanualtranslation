from htmlparser import MyHTMLParser
from re import sub
from urllib.parse import unquote_plus as translate_url


class BaseItem:
    """
    Holds the basic item (post, tag, media and so on data. DO NOT USE directly. For inheritance only
    """
    def __init__(self, str_id: str, str_name: str, str_content: str, str_link: str):
        # Class vars
        self.id = str_id
        # parse url decoding
        self.name = translate_url(str_name)
        self.name_small_list = list()
        self.content = list()
        self.link = str_link

        # Strip unneeded html tags from post content
        html_remover = MyHTMLParser()
        html_remover.feed(str_content)

        # Strip remaining non HTML tags (such as [h5p id="#"])
        for item in html_remover.html_text:
            temp = sub(r" ?\[[^)]+\]", "****h5p_item****", item)
            self.content.append(temp)

        html_remover.close()
