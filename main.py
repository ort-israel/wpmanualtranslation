import settings
import csvparser
import post
import outputcreator


def main():
    """Main func"""

    # Read settings
    settings_dict = settings.read_settings()

    # Get list of posts
    list_of_posts = csvparser.csv_reader(settings_dict["csv_name"],
                                         settings_dict["mark_start"],
                                         settings_dict["mark_end"])

    # Send posts to the formatter
    outputcreator.text_output(list_of_posts, settings_dict["project"])

    # Print done
    print(settings_dict["project"] + " is Done!")


if __name__ == "__main__":
    main()
