"""    <Simple tool to manually find string that need to be translated in a wordpress for cases where you chose to duplicate the site>
    Copyright (C) <2020>  <Shay Gover, ort-israel>

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
