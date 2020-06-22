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
from settings import *
import csvparser
import outputcreator
from plugins import load_plugins


def main():
    """Main func"""

    # Print license
    print(" <wpmanualtranslation>  Copyright (C) <2020>  <Shay Gover, ort-israel>")
    print("This program comes with ABSOLUTELY NO WARRANTY; ")
    print("This is free software, and you are welcome to redistribute ")
    print("it under certain conditions; For more details check the repo:")
    print("https://github.com/ort-israel/wpmanualtranslation")

    # Read settings
    read_settings()

    # Get list of posts
    list_of_posts_type = csvparser.post_csv_reader(settings_dict["posts_csv_name"])
    list_of_posts = outputcreator.sort_item_type(list_of_posts_type, POST_TYPE)
    list_of_pages = outputcreator.sort_item_type(list_of_posts_type, PAGE_TYPE)
    list_of_media = outputcreator.sort_item_type(list_of_posts_type, MEDIA_TYPE)
    list_of_nav_items = outputcreator.sort_item_type(list_of_posts_type, NAV_MENU_ITEM_TYPE)

    # Get list of tags
    list_of_tags_type = csvparser.tag_csv_reader()
    list_of_tags = outputcreator.sort_item_type(list_of_tags_type, TAG_TYPE)
    list_of_categories = outputcreator.sort_item_type(list_of_tags_type, CATEGORY_TYPE)
    list_of_nav_menu = outputcreator.sort_item_type(list_of_tags_type, NAV_MENU_TYPE)

    # Plugin types - tags

    # Plugin types - posts
    list_of_cf7 = outputcreator.sort_item_type(list_of_posts_type, CF7_TYPE)
    list_of_gloss = outputcreator.sort_item_type(list_of_posts_type, CM_TOOLTIP_GLOSSARY_TYPE)

    # Send items to the formatter
    outputcreator.post_text_output(list_of_posts, "Posts")
    outputcreator.post_text_output(list_of_media, "Media")
    outputcreator.post_text_output(list_of_pages, "Pages")
    outputcreator.tag_text_output(list_of_tags, "Tags")
    outputcreator.tag_text_output(list_of_categories, "Categories")
    outputcreator.tag_text_output(list_of_nav_menu, "Nav Menus")
    outputcreator.nav_text_output(list_of_nav_items)

    # WP Plugins
    outputcreator.post_text_output(list_of_gloss, "CM Tooltip Glossary")
    outputcreator.post_text_output(list_of_cf7, "Contact Form 7")

    """
    Plugins made my life harder. Therefore counter productive
    # Load plugins
    if settings_dict["plugins"]:
        load_plugins(list_of_posts_type, list_of_tags_type)
    """

    # Print done
    print(settings_dict["project"] + " is Done!")


if __name__ == "__main__":
    main()
