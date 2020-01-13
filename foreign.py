from guess_language import guess_language
import enchant


def word_breaker(str_sentence: str) -> list:
    """
    Breaks a list to words by spaces.
    :param str_sentence: string to break
    :return: list of words
    """
    return str_sentence.split()


def lang_marker(list_of_words: list, str_start_mark: str, str_end_mark: str, lang: str):
    """
    Checks if str_list contains lang words.
    :param list_of_words: Post content as a list of words.
    :param str_start_mark: Something to put before an Hebrew words
    :param str_end_mark: Something to put after
    :param lang: Language to mark
    :return: 1) complete_list: List of all words, Hebrew words are marked by str_start_mark and str_end_mark. (Within that
                list item). so: ["non Hebrew", "str_start_mark Hebrew str_end_mark", .....]
             2) small_list: List of Hebrew words. No marking.
    """
    complete_list = list()
    small_list = list()

    # Check all words
    for str_cell in list_of_words:
        # Adding /r and /n
        # Change ř to \r . Then ň to \n
        str_text = str_cell.replace("ř", "\r")
        str_text = str_text.replace("ň", "\n")

        # If hebrew add marking.
        if guess_language(str_text) == lang:
            # Note: In python only functions, modules and classes have scope
            temp = str_start_mark + str_text + str_end_mark
            small_list.append(str_text)
        else:
            temp = str_text

        complete_list.append(temp)

    return complete_list, small_list
