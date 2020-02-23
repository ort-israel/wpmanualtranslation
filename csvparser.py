from csv import reader
from post import Post
from tag import Tag
from settings import settings_dict


def post_csv_reader(str_file_name: str):
    """
    Parses the csv file and returns a list of post objects
    :param str_file_name: file name
    :return: list of posts, pages or media
    """
    list_of_post = list()

    with open(str_file_name, newline='', encoding='utf_8') as posts:
        posts_reader = reader(posts, delimiter='‡', quotechar='|')
        # To get rid of the first line: ['ID', 'post_content', 'post_title', 'post_excerpt', 'post_name', 'guid']
        posts_reader.__next__()
        # Create a post class for each line and push it to the return list
        for current_post in posts_reader:
            post_obj = Post(current_post[0], current_post[1], current_post[2], current_post[3],
                            current_post[4], current_post[5], settings_dict["mark_start"], settings_dict["mark_end"])
            list_of_post.append(post_obj)

    # Return the list
    return list_of_post


def tag_csv_reader():
    """
        Parses the csv file and returns a list of tag objects
        :return: list of tags and categories
    """
    list_of_tags = list()

    with open(settings_dict["tag_csv_name"], newline='', encoding='utf_8') as tags:
        tags_reader = reader(tags, delimiter='‡', quotechar='|')
        # To get rid of the first line: ['term_id', 'name', 'slug', 'taxonomy', 'description']
        tags_reader.__next__()
        # Create a tag class for each line and push it to the return list
        # num_id: str, str_name: str, str_slug: str, str_type: str, str_desc: str
        for current_tag in tags_reader:
            tag_obj = Tag(current_tag[0], current_tag[1], current_tag[2], current_tag[3],
                          current_tag[4], settings_dict["mark_start"], settings_dict["mark_end"])
            list_of_tags.append(tag_obj)

    # Return the list
    return list_of_tags
