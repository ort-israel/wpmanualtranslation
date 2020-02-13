from settings import settings_dict
import csvparser
import post
import outputcreator


def main():
    """Main func"""

    # Read settings
    settings.read_settings()

    # Get list of posts
    list_of_posts = csvparser.post_csv_reader()

    # Get list of media (pictures an so on)
    list_of_media = csvparser.post_csv_reader()

    # Get list of tags
    list_of_tags = csvparser.tag_csv_reader()

    # Get list of menu items
    list_of_nav = csvparser.post_csv_reader()

    # Send items to the formatter
    outputcreator.post_text_output(list_of_posts, settings_dict["project"], "Posts and Pages")
    outputcreator.post_text_output(list_of_media, settings_dict["project"], "Media")
    outputcreator.tag_text_output(list_of_tags, settings_dict["project"])
    outputcreator.nav_text_output(list_of_nav, settings_dict["project"])

    # Print done
    print(settings_dict["project"] + " is Done!")


if __name__ == "__main__":
    main()
