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
from csv import reader
from post import *
from tag import *
from settings import settings_dict


def post_csv_reader(str_file_name: str):
    """
    Parses the csv file and returns a list of objects
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
                            current_post[4], current_post[5], current_post[6])

            # Making sure that items that don't need translation won't be printed to output
            if post_obj.is_post_translation_needed():
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
                          current_tag[4])

            # Making sure that items that don't need translation won't be printed to output
            if tag_obj.is_tag_translation_needed():
                list_of_tags.append(tag_obj)

    # Return the list
    return list_of_tags
