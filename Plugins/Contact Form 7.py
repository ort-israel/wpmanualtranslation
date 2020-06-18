""" <Simple tool to manually find string that need to be translated in a wordpress for cases where you chose to duplicate the site>
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

"""
This plugin parses strings from Contact Form 7:
https://wordpress.org/plugins/contact-form-7/

To use this plugin add "Contact Form 7" to config.txt. See README for more details.

This plugin has one post type (no tags): wpcf7_contact_form
"""
from outputcreator import post_text_output

CF7_TYPE = "wpcf7_contact_form"


def main_plug(list_of_posts_type: list, list_of_tags_type: list):
    """
    Main func for contact form 7 plugin
    :param list_of_posts_type: list of post items type
    :param list_of_tags_type: list of tag items type. Not used
    :return: nothing
    """
    # Get relevant glossary items
    list_of_cf7 = sort_cf7_type(list_of_posts_type)

    # Print it
    post_text_output(list_of_cf7, "Contact Form 7")


def sort_cf7_type(obj_list: list):
    """
    Creates a new list with GLOSSARY_TYPE objects.
    :param obj_list: list of item objects
    :return: list of object containing only GLOSSARY_TYPE items
    """
    by_type_list = list()
    sorted_list = list()

    for current_obj in obj_list:
        if current_obj.type == CF7_TYPE:
            by_type_list.append(current_obj)

    # Sort certain object list by ABC
    sorted_list = sorted(by_type_list, key=lambda post: post.title)

    return sorted_list

