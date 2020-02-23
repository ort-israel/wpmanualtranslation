from baseitem import BaseItem
import foreign


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
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, "ar")

        # Mark foreign words in name
        words = self.name.split("-")
        to_discard, self.name_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, "ar")

        # Mark foreign words in title
        words = foreign.word_breaker(self.name)
        to_discard, self.title_small_list = \
            foreign.content_lang_marker(words, str_mark_start, str_mark_end, "ar")

