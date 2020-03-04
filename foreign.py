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
from guess_language import guess_language
from settings import settings_dict
from unicodedata import name as writing_system


def is_word_system_bad(str_word: str) -> bool:
    """
    Detects the writing system of a str_word
    :param str_word: word to check
    :return: True if the word needs to be translated, False otherwise
    """
    # Make sure the word is not an h5p or image place holder
    if str_word == settings_dict["h5p"] or str_word == settings_dict["image"]:
        return False

    # Iterate on the word. If it's number - ignore and move on. If char check writing system
    for char in str_word:
        system = writing_system(char, "error").split()[0]
        if system == "error" and str.isprintable(char):
            raise Exception("Unknown writing system: " + str_word + " ||| " + char)
        elif system != settings_dict["writing_system"] and str.isalpha(char):
            return True

    # If it got here, it should be ok
    return False


def content_lang_marker(list_of_words: list):
    """
    Checks if str_list contains lang words.
    :param list_of_words: Post content as a list of words.
    :return: 1) complete_list: List of all words, Hebrew words are marked by str_start_mark and str_end_mark.
                (Within that list item). so: ["non Hebrew", "str_start_mark Hebrew str_end_mark", .....]
             2) small_list: List of Hebrew words. No marking.
    """
    complete_list = list()
    small_list = list()
    sentence_list = list()  # Creates list of segments by writing system
    str_sentence = ""

    # Check all words
    for str_cell in list_of_words:
        # Adding /r and /n (Python delimiter workaround)
        # Change ř to \r . Then ň to \n
        str_text = str_cell.replace("ř", "\r")
        str_text = str_text.replace("ň", "\n")

        # Check if word needs translation, add it only if it's not empty
        if is_word_system_bad(str_text):
            str_sentence += str_text + " "
        elif len(str_sentence) > 0:
            sentence_list.append(str_sentence)
            str_sentence = ""
    else:
        # Append the last sentence to the list unless it's already there. Add only if it's not empty
        if str_sentence.isprintable() and len(str_sentence) > 0:
            try:
                str_last = sentence_list[-1]

                if str_last != str_sentence:
                    sentence_list.append(str_sentence)
            except IndexError:
                sentence_list.append(str_sentence)

    for str_cell in sentence_list:
        # If foreign add marking.
        if guess_language(str_cell) != settings_dict["language"]:
            # Note: In python only functions, modules and classes have scope
            temp = settings_dict["mark_start"] + " " + str_cell + " " + settings_dict["mark_end"]
            small_list.append(str_cell)
        else:
            temp = str_cell

        complete_list.append(temp)

    return complete_list, small_list
