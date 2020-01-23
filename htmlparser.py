from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """This is my implementation of HTMLParser. Ignores everything but data"""
    def __init__(self):
        # In this list all the data will be saved
        super().__init__()
        self.html_text = list()

    def handle_data(self, data):
        """

        :param data: Non html string
        :return: Appends the non html data to html_text
        """
        self.html_text.append(data)

    def handle_starttag(self, tag, attrs):
        """

        :param tag:
        :param attrs:
        :return: Appends img tags to html_txt
        """
        if tag == "img":
            self.html_text.append("ň****Image****ň")


def get_sections(str_content):
    """
    **** Don't use!!! Elementor doesn't divide the code by div, span or anything else.
    Divides a post into section by Divs
    :param str_content: Post content
    :returns: list of sections
    """
    pass



