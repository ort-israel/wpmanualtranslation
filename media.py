from baseitem import BaseItem


class Media(BaseItem):
    """
    This class holds media items (pictures).
    """
    def __init__(self, str_id: str, str_title: str, str_content: str, str_excerpt: str, str_name: str, str_link: str):
        super().__init__(str_id, str_name, str_content, str_link)
        # Here be class vars.
        # str_link hold guid

