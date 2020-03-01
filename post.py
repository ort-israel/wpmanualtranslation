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
# Imports
from htmlparser import *
from re import sub
import foreign
from urllib.parse import unquote_plus as translate_url
from settings import settings_dict
from baseitem import *


# Post class
class Post(BaseItem):
    """
    Holds a single post, page or media data
    """

    def __init__(self, num_id: str, str_content: str, str_title: str, str_excerpt: str, str_name: str, str_guid: str,
                 str_type: str, str_mark_start: str, str_mark_end: str):
        # Here be all class vars
        super().__init__(num_id, str_name, str_content, str_guid, str_type)
        self.title = str_title  # Post title
        self.title_small_list = list()
        self.excerpt = str_excerpt  # Post excerpt
        self.name = translate_url(str_name)  # Post name
        self.name_small_list = list()
        self.content_small_list = list()
        self.content_complete_list = list()
        self.excerpt_small_list = list()
        self.excerpt_complete_list = list()

        words = list()

        # Mark foreign words in content
        for post_text in self.content:
            words += foreign.word_breaker(post_text)
        self.content_complete_list, self.content_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, settings_dict["language"])

        words = foreign.word_breaker(self.excerpt)

        # Mark foreign words in excerpt
        self.excerpt_complete_list, self.excerpt_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, settings_dict["language"])

        # Mark foreign words in name
        words = self.name.split("-")
        to_discard, self.name_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, settings_dict["language"])

        # Mark foreign words in title
        words = foreign.word_breaker(self.title)
        to_discard, self.title_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, settings_dict["language"])
