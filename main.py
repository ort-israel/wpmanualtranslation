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
    list_of_posts = csvparser.post_csv_reader(settings.settings_dict["posts_csv_name"])

    # Get list of media (pictures an so on)
    list_of_media = csvparser.post_csv_reader(settings.settings_dict["media_csv_name"])

    # Get list of tags
    list_of_tags = csvparser.tag_csv_reader()

    # Get list of menu items
    list_of_nav = csvparser.post_csv_reader(settings.settings_dict["nav_csv_name"])

    # Send items to the formatter
    outputcreator.post_text_output(list_of_posts, settings.settings_dict["project"], "Posts and Pages")
    outputcreator.post_text_output(list_of_media, settings.settings_dict["project"], "Media")
    outputcreator.tag_text_output(list_of_tags, settings.settings_dict["project"])
    outputcreator.nav_text_output(list_of_nav, settings.settings_dict["project"])

    # Print done
    print(" <wpmanualtranslation>  Copyright (C) <2020>  <Shay Gover, ort-israel>")
    print("This program comes with ABSOLUTELY NO WARRANTY; ")
    print("This is free software, and you are welcome to redistribute ")
    print("it under certain conditions; For more details check the repo:")
    print("https://github.com/ort-israel/wpmanualtranslation")
    print(settings.settings_dict["project"] + " is Done!")


if __name__ == "__main__":
    main()
