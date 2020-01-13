# Fields are separated by ;="
from csv import reader
from post import Post


def csv_reader(csv_file_name):
    """
    Pasrses the csv file and returns a list of post objects
    :param csv_file_name: csv file name. should be in the same dir
    :return: list of posts
    """
    list_of_post = list()

    with open(csv_file_name, newline='', encoding='utf_8') as posts:
        posts_reader = reader(posts, delimiter='‡', quotechar='|')
        # To get rid of the first line: ['ID', 'post_content', 'post_title', 'post_excerpt', 'post_name', 'guid']
        posts_reader.__next__()
        # Create a post class for each line and push it to the return list
        for current_post in posts_reader:
            # Change ř to \r . Then ň to \n
            # content = current_post[1]
            # content = content.replace("ř", "\r")
            # content = content.replace("ň", "\n")

            post_obj = Post(current_post[0], current_post[1], current_post[2],
                            current_post[3], current_post[4], current_post[5])
            list_of_post.append(post_obj)

    # Return the list
    return list_of_post
