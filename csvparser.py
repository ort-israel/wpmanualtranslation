# Fields are separated by ;="
from csv import reader
from post import Post
from tag import Tag


def post_csv_reader(csv_file_name: str, str_mark_start: str, str_mark_end: str):
    """
    Parses the csv file and returns a list of post objects
    :param csv_file_name: csv file name. should be in the same dir
    :param str_mark_start: Mark string prefix
    :param str_mark_end: Mark string postfix
    :return: list of posts, pages or media
    """
    list_of_post = list()

    with open(csv_file_name, newline='', encoding='utf_8') as posts:
        posts_reader = reader(posts, delimiter='‡', quotechar='|')
        # To get rid of the first line: ['ID', 'post_content', 'post_title', 'post_excerpt', 'post_name', 'guid']
        posts_reader.__next__()
        # Create a post class for each line and push it to the return list
        for current_post in posts_reader:
            post_obj = Post(current_post[0], current_post[1], current_post[2], current_post[3],
                            current_post[4], current_post[5], str_mark_start, str_mark_end)
            list_of_post.append(post_obj)

    # Return the list
    return list_of_post


def tag_csv_reader(csv_file_name: str, str_mark_start: str, str_mark_end: str):
    """
        Parses the csv file and returns a list of tag objects
        :param csv_file_name: csv file name. should be in the same dir
        :param str_mark_start: Mark string prefix
        :param str_mark_end: Mark string postfix
        :return: list of tags and categories
    """
    list_of_tags = list()

    with open(csv_file_name, newline='', encoding='utf_8') as tags:
        tags_reader = reader(tags, delimiter='‡', quotechar='|')
        # To get rid of the first line: ['term_id', 'name', 'slug', 'taxonomy', 'description']
        tags_reader.__next__()
        # Create a tag class for each line and push it to the return list
        # num_id: str, str_name: str, str_slug: str, str_type: str, str_desc: str
        for current_tag in tags_reader:
            tag_obj = Post(current_tag[0], current_tag[1], current_tag[2], current_tag[3],
                           current_tag[4], str_mark_start, str_mark_end)
            list_of_tags.append(tag_obj)

    # Return the list
    return list_of_tags
