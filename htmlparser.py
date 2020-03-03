"""    <Simple tool to manually find string that need to be translated in a wordpress for cases where you chose to duplicate the site>
    Copyright (C) <2020>  <Shay     Copyright (C) <2020>  <Shay Gover, ort-israel>
>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""
from html.parser import HTMLParser
from settings import settings_dict


class MyHTMLParser(HTMLParser):
    """This is my implementation of HTMLParser. Ignores everything but data"""
    def __init__(self):
        # In this list all the data will be saved
        super().__init__()
        self.html_text = ""

    def handle_data(self, data):
        """

        :param data: Non html string
        :return: Appends the non html data to html_text
        """
        self.html_text += data

    def handle_starttag(self, tag, attrs):
        """

        :param tag:
        :param attrs:
        :return: Appends img tags to html_txt
        """
        if tag == "img":
            self.html_text += " " + settings_dict["image"] + " "


def get_sections(str_content):
    """
    **** Don't use!!! Elementor doesn't divide the code by div, span or anything else.
    Divides a post into section by Divs
    :param str_content: Post content
    :returns: list of sections
    """
    pass



