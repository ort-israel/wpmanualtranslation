# Fields are separated by ;="
from csv import reader


# file name. Should be in the same dir
str_csv_file_name = "wp_posts_unicode.csv"

with open(str_csv_file_name, newline='', encoding='utf_8') as posts:
    posts_reader = reader(posts, delimiter='‡', quotechar='|')
    # To get rid of the first line: ['ID', 'post_content', 'post_title', 'post_excerpt', 'post_name', 'guid']
    posts_reader.__next__()
    # each row is an array. So a[0] will give the post id and so one. Use a loop to iterate
    # Add all this code to a function that returns a post class

