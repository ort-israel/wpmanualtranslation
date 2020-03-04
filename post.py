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
import foreign
from settings import *
from baseitem import *


# Post class
class Post(BaseItem):
    """
    Holds a single post, page or media data
    """

    def __init__(self, num_id: str, str_content: str, str_title: str, str_excerpt: str, str_name: str, str_guid: str,
                 str_type: str):
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

        # Mark foreign words in content
        self.content_complete_list, self.content_small_list = \
            foreign.content_lang_marker(self.content.split(" "))

        # Mark foreign words in excerpt
        self.excerpt_complete_list, self.excerpt_small_list = \
            foreign.content_lang_marker(self.excerpt.split(" "))

        # Mark foreign words in name unless it's nav menu item
        if self.type != NAV_MENU_ITEM_TYPE:
            to_discard, self.name_small_list = \
                foreign.content_lang_marker(self.name.split("-"))

        # Mark foreign words in title
        to_discard, self.title_small_list = \
            foreign.content_lang_marker(self.title.split(" "))

    def is_post_translation_needed(self):
        """
        Checks if post object type needs translation
        :param self: post object
        :return: True if translation needed, False otherwise
        """
        if self.type == PAGE_TYPE:
            if len(self.excerpt_small_list) > 0 or len(self.content_small_list) > 0 or \
                   len(self.name_small_list) > 0 or len(self.title_small_list) > 0:
                return True
        elif self.type == POST_TYPE:
            if len(self.excerpt_small_list) > 0 or len(self.content_small_list) > 0 or \
                    len(self.name_small_list) > 0 or len(self.title_small_list) > 0:
                return True
        elif self.type == MEDIA_TYPE:
            if len(self.excerpt_small_list) > 0 or len(self.content_small_list) > 0 or \
                    len(self.name_small_list) > 0 or len(self.title_small_list) > 0:
                return True
        elif self.type == NAV_MENU_ITEM_TYPE:
            # For nav menu items, name is useless
            if len(self.excerpt_small_list) > 0 or len(self.content_small_list) > 0 or \
                    len(self.title_small_list) > 0:
                return True
        else:
            raise Exception("Unknown post type: " + self.type)

        return False
