import settings
import csvparser


def main():
    """Main func"""

    # Read settings
    settings_dict = settings.read_settings()

    # Get list of posts
    list_of_posts = csvparser.csv_reader(settings_dict["csv_name"])

    # Run on all the posts, break each post content string to words and get the foreign lists.
    # Should add 2 new post class vars: for the complete list and for the small list
    # Then print them nicely. Maybe add a new file for that: outputcreator.py. for v0.1 just txt
    # For the complete list: each post in its own file.
    # For the small list: same file with a ******* separator.


