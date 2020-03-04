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
import settings
import csvparser
import outputcreator


def main():
    """Main func"""

    # Read settings
    settings.read_settings()

    # Get list of posts
    list_of_posts_type = csvparser.post_csv_reader(settings.settings_dict["posts_csv_name"])
    list_of_posts = outputcreator.sort_item_type(list_of_posts_type, settings.POST_TYPE)
    list_of_pages = outputcreator.sort_item_type(list_of_posts_type, settings.PAGE_TYPE)

    # Get list of media (pictures an so on)
    list_of_media = csvparser.post_csv_reader(settings.settings_dict["media_csv_name"])

    # Get list of tags
    list_of_tags_type = csvparser.tag_csv_reader()
    list_of_tags = outputcreator.sort_item_type(list_of_tags_type, settings.TAG_TYPE)
    list_of_categories = outputcreator.sort_item_type(list_of_tags_type, settings.CATEGORY_TYPE)
    list_of_glossaries = outputcreator.sort_item_type(list_of_tags_type, settings.GLOSSARY_TYPE)
    list_of_nav_menu = outputcreator.sort_item_type(list_of_tags_type, settings.NAV_MENU_TYPE)

    # Get list of menu items
    list_of_nav = csvparser.post_csv_reader(settings.settings_dict["nav_csv_name"])

    # Send items to the formatter
    outputcreator.post_text_output(list_of_posts, "Posts")
    outputcreator.post_text_output(list_of_media, "Media")
    outputcreator.post_text_output(list_of_pages, "Pages")
    outputcreator.tag_text_output(list_of_tags, "Tags")
    outputcreator.tag_text_output(list_of_categories, "Categories")
    outputcreator.tag_text_output(list_of_glossaries, "Glossary Categories")
    outputcreator.tag_text_output(list_of_nav_menu, "Nav Menus")
    outputcreator.nav_text_output(list_of_nav)

    # Print done
    print(" <wpmanualtranslation>  Copyright (C) <2020>  <Shay Gover, ort-israel>")
    print("This program comes with ABSOLUTELY NO WARRANTY; ")
    print("This is free software, and you are welcome to redistribute ")
    print("it under certain conditions; For more details check the repo:")
    print("https://github.com/ort-israel/wpmanualtranslation")
    print(settings.settings_dict["project"] + " is Done!")


if __name__ == "__main__":
    main()
