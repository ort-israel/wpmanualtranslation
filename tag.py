import foreign
from re import sub


class Tag:
    """
        Holds a single tag, category or nav menu item data
    """

    def __init__(self, num_id: str, str_name: str, str_slug: str, str_type: str, str_desc: str,
                 str_mark_start: str, str_mark_end: str):
        # Here be all class vars
        self.id = num_id  # ID
        self.name = str_name  # Item name
        self.filtered_name = list()  # Name without number, split by -
        self.url = str_slug  # Item url. Not a real url. Contains char codes %## Probably useless
        self.type = str_type  # Item type (tag, category or nav menu item)
        self.description = str_desc.split()  # Item description. Split on spaces and line break
        self.desc_small_list = list()
        self.desc_complete_list = list()
        self.name_small_list = list()
        self.name_complete_list = list()

        # Filter item name
        # https://docs.python.org/3/library/re.html
        self.filtered_name = sub(r"[0-9]+?", "", self.name).split("-")

        # Mark foreign words in descriptions
        self.desc_complete_list, self.desc_small_list = \
            foreign.content_lang_marker(self.description, str_mark_start, str_mark_end, "he")

        # Mark foreign words in the name
        self.name_complete_list, self.name_small_list = \
            foreign.content_lang_marker(self.filtered_name, str_mark_start, str_mark_end, "he")

