from baseitem import BaseItem
import foreign


class Media(BaseItem):
    """
    This class holds media items (pictures).
    """
    def __init__(self, str_id: str, str_title: str, str_content: str, str_excerpt: str, str_name: str, str_link: str):
        super().__init__(str_id, str_name, str_content, str_link)
        # Here be class vars.
        # str_link hold guid
        self.excerpt = str_excerpt
        self.title = str_title

        words = foreign.word_breaker(self.excerpt)

        # Mark foreign words in excerpt
        self.excerpt_complete_list, self.excerpt_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, "he")

