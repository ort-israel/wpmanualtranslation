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
import foreign
from re import sub
from baseitem import BaseItem
from settings import settings_dict


class Tag(BaseItem):
    """
        Holds a single tag, category or nav menu item data
    """

    def __init__(self, num_id: str, str_name: str, str_slug: str, str_type: str, str_desc: str, str_mark_start: str,
                 str_mark_end: str):
        super().__init__(num_id, str_name, str_desc, str_slug, str_type)
        # Here be all class vars
        self.filtered_name = list()  # Name without number, split by -
        # str_slug is not a real url. Contains char codes %##. Probably useless
        self.description = list()  # Item description. Split on spaces and line break
        self.desc_small_list = list()
        self.desc_complete_list = list()
        self.name_small_list = list()
        self.name_complete_list = list()

        # Split content by spaces
        for str_item in self.content:
            self.description.extend(str_item.split(" "))
        # Filter item name
        # https://docs.python.org/3/library/re.html
        self.filtered_name = sub(r"[0-9]+?", "", self.name).split("-")

        # Mark foreign words in descriptions
        self.desc_complete_list, self.desc_small_list = \
            foreign.content_lang_marker(self.description, str_mark_start, str_mark_end, settings_dict["language"])

        # Mark foreign words in the name
        self.name_complete_list, self.name_small_list = \
            foreign.content_lang_marker(self.filtered_name, str_mark_start, str_mark_end, settings_dict["language"])
