import settings
import csvparser
import post
import outputcreator


def main():
    """Main func"""

    # Read settings
    settings_dict = settings.read_settings()

    # Get list of posts
    list_of_posts = csvparser.csv_reader(settings_dict["posts_csv_name"],
                                         settings_dict["mark_start"],
                                         settings_dict["mark_end"])

    # Get list of media (pictures)
    list_of_media = csvparser.csv_reader(settings_dict["media_csv_name"],
                                         settings_dict["mark_start"],
                                         settings_dict["mark_end"])

    # Send items to the formatter
    outputcreator.post_text_output(list_of_posts, settings_dict["project"], "Posts and Pages")
    outputcreator.post_text_output(list_of_media, settings_dict["project"], "Media")

    # Print done
    print(settings_dict["project"] + " is Done!")


if __name__ == "__main__":
    main()
