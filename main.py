import settings
import csvparser
import post
import outputcreator


def main():
    """Main func"""

    # Read settings
    settings_dict = settings.read_settings()

    # Get list of posts
    list_of_posts = csvparser.csv_reader(settings_dict["csv_name"])

    # Send posts to the formatter
    outputcreator.text_output(list_of_posts, "Money")


if __name__ == "__main__":
    main()
