from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """This is my implementation of HTMLParser. Ignores everything but data"""
    # In this list all the data will be saved
    html_text = list()

    def handle_data(self, data):
        """

        :param data: Non html string
        :return: Appends the non html data to html_text
        """
        self.html_text.append(data + " ")


def square_stripper(data):
    """
    Strips bbcode style tags from the text
    :param data: string to strip
    :return: string without bbcode style tags
    """
    pass


def get_sections(str_content):
    """
    **** Don't use!!! Elementor doesn't divide the code by div, span or anything else.
    Divides a post into section by Divs
    :param str_content: Post content
    :returns: list of sections
    """
    pass


def strip_html(string_to_strip):
    """
    Strip html tags from string
    :param string_to_strip: target string.
    :return: string without non relevant html tags.
    Discarded tags: iframe, h5p ([h5p id="##"]), img
    """
    pass




