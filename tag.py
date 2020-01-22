import foreign
from re import sub
from baseitem import BaseItem


class Tag(BaseItem):
    """
        Holds a single tag, category or nav menu item data
    """

    def __init__(self, num_id: str, str_name: str, str_slug: str, str_type: str, str_desc: str, str_mark_start: str,
                 str_mark_end: str):
        super().__init__(num_id, str_name, str_desc, str_slug)
        # Here be all class vars
        self.filtered_name = list()  # Name without number, split by -
        # str_slug is not a real url. Contains char codes %##. Probably useless
        self.type = str_type  # Item type (tag, category or nav menu item)
        self.description = super().content.split()  # Item description. Split on spaces and line break
        self.desc_small_list = list()
        self.desc_complete_list = list()
        self.name_small_list = list()
        self.name_complete_list = list()

        # Filter item name
        # https://docs.python.org/3/library/re.html
        self.filtered_name = sub(r"[0-9]+?", "", super().name).split("-")

        # Mark foreign words in descriptions
        self.desc_complete_list, self.desc_small_list = \
            foreign.content_lang_marker(self.description, str_mark_start, str_mark_end, "he")

        # Mark foreign words in the name
        self.name_complete_list, self.name_small_list = \
            foreign.content_lang_marker(self.filtered_name, str_mark_start, str_mark_end, "he")
