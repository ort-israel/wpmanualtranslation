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
from baseitem import BaseItem
import foreign
from settings import settings_dict


class Media(BaseItem):
    """
    This class holds media items (pictures).
    """
    def __init__(self, str_id: str, str_title: str, str_content: str,
                 str_excerpt: str, str_name: str, str_link: str, str_mark_start: str, str_mark_end: str):
        super().__init__(str_id, str_name, str_content, str_link)
        # Here be class vars.
        # str_link hold guid
        self.excerpt = str_excerpt
        self.title = str_title
        self.title_small_list = list()

        # Mark foreign words in excerpt
        words = foreign.word_breaker(self.excerpt)
        self.excerpt_complete_list, self.excerpt_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, settings_dict["media_csv_name"])

        # Mark foreign words in name
        words = self.name.split("-")
        to_discard, self.name_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, settings_dict["media_csv_name"])

        # Mark foreign words in title
        words = foreign.word_breaker(self.name)
        to_discard, self.title_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, settings_dict["media_csv_name"])

