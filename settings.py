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

# Item types constants
POST_TYPE = "post"
PAGE_TYPE = "page"
MEDIA_TYPE = "attachment"
TAG_TYPE = "post_tag"
CATEGORY_TYPE = "category"
NAV_MENU_TYPE = "nav_menu"
GLOSSARY_TYPE = "glossary-cat"
NAV_MENU_ITEM_TYPE = "nav_menu_item"

# Holds all settings <=
settings_dict = {"posts_csv_name": "Def",
                 "media_csv_name": "Def"}


def lang_to_system(str_lang: str) -> str:
    """
    Converts language to writing system
    :param str_lang: Target new site language
    :return: Writing system of str_lang
    """
    # Use writing_system("<char>").split()[0] to add new languages
    if str_lang == "he":
        return "HEBREW"
    elif str_lang == "en" or str_lang == "fr":
        return "LATIN"
    elif str_lang == "ar":
        return "ARABIC"
    else:
        raise Exception("Unknown language")


def read_settings():
    """Read settings from the config file and populates settings_dict
    List of possible settings:
    posts_csv_name: post and pages csv file name
    media_csv_name: media csv file name
    tag_csv_name: Tags and categories file name
    nav_csv_name: Nav menu items file name
    mark_start: Mark start
    mark_end: Mark end
    project: Project name. Will be used as output folder name and small file name
    language: Language needed
    image: image placeholder
    h5p: h5p placeholder
    """

    with open("config.txt") as settings_file:
        for line in settings_file:
            if not(line.startswith("#")) and not(line == ""):
                # Remove end of line char
                line = line.strip("\n")

                # Splitting on :=
                key, value = line.split(":=")
                settings_dict[key] = value

    # Set writing system
    settings_dict["writing_system"] = lang_to_system(settings_dict["language"])

    # Make sure that all required settings were loaded