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
import os
from settings import *


def tag_text_output(list_of_tags: list, str_type):
    """
    Prints tag item type to file
    :param str_type: Subdirectory name. Should be tags
    :param list_of_tags: All the tags to print.
    :return:
    """
    # Check the folder exists
    # Open the small list file for writing and clear it
    folder_maker(settings_dict["project"])
    folder_maker(str_type)
    small_file = open("00" + settings_dict["project"] + "-" + str_type + ".txt", "w")

    # Iterate on tags, create files for the complete list and append for the small list
    for single_item in list_of_tags:
        # Complete list
        complete_file = open(single_item.name + ".txt", "w")
        complete_file.write("--------------------------------------------------------------------------------- \n")
        complete_file.write("Name: ... " + single_item.name + "\n")
        complete_file.write("Marked Name: ... " + " ".join(single_item.name_complete_list) + "\n")
        complete_file.write("--------------------------------------------------------------------------------- \n \n")
        complete_file.write("--------------------------------------------------------------------------------- \n \n")
        complete_file.write(" ".join(single_item.desc_complete_list))

        # Close the complete file
        complete_file.close()

        # Small file
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")
        small_file.write("--------------- \n")
        small_file.write("Name: ... " + single_item.name + "\n")
        small_file.write("Marked Name: ... " + " ".join(single_item.name_small_list) + "\n")
        small_file.write("--------------- \n \n")
        small_file.write(" ".join(single_item.desc_small_list) + "\n")
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")

    # Close the small file
    small_file.close()

    # Return to root folder
    return_to_root()


def post_text_output(list_of_items: list, str_type: str):
    """
    Prints the results to files.
    Small list goes into a single file with ********** separator between posts. File name is 00<folder_name>
    Complete list: Each post gets it's own file
    :param str_type: Type of items: Posts and pages or Media
    :param list_of_items: All the posts
    :return:
    """
    # Check the folder exists
    # Open the small list file for writing and clear it
    folder_maker(settings_dict["project"])
    folder_maker(str_type)
    small_file = open("00" + settings_dict["project"] + "-" + str_type + ".txt", "w")

    # Iterate on posts, create files for the complete list and append for the small list
    for single_item in list_of_items:
        # Complete list
        complete_file = open(single_item.title + ".txt", "w")
        complete_file.write("--------------------------------------------------------------------------------- \n")
        complete_file.write("Title: ... " + single_item.title + "\n")
        complete_file.write("Title foreign parts: ... " + " ".join(single_item.title_small_list) + "\n")
        complete_file.write("Name: ... " + single_item.name + "\n")
        complete_file.write("Name foreign parts: ... " + " ".join(single_item.name_small_list) + "\n")
        complete_file.write("Link: ... " + single_item.link + "\n")
        complete_file.write("--------------------------------------------------------------------------------- \n \n")
        complete_file.write("Excerpt: \n")
        complete_file.write(" ".join(single_item.excerpt_complete_list))
        complete_file.write("--------------------------------------------------------------------------------- \n \n")
        complete_file.write(" ".join(single_item.content_complete_list))

        # Close the complete file
        complete_file.close()

        # Small file
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")
        small_file.write("--------------- \n")
        small_file.write("Title: ... " + single_item.title + "\n")
        small_file.write("Title foreign parts: ... " + " ".join(single_item.title_small_list) + "\n")
        small_file.write("Name: ... " + single_item.name + "\n")
        small_file.write("Name foreign parts: ... " + " ".join(single_item.name_small_list) + "\n")
        small_file.write("Link: ... " + single_item.link + "\n")
        small_file.write("Excerpt: ... " + " ".join(single_item.excerpt_small_list) + "\n")
        small_file.write("--------------- \n \n")
        small_file.write(" ".join(single_item.content_small_list) + "\n")
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")

    # Close the small file
    small_file.close()

    # Return to root folder
    return_to_root()


def nav_text_output(list_of_items: list):
    """
    Prints the menu items to a single file (Only item name, title and id are relevant)
    :param list_of_items: list of menu item. Type is post class
    :return: Prints everything to a file called nav_menu_items.txt
    """
    # Check the folder exists
    # Open the small list file for writing and clear it
    folder_maker(settings_dict["project"])
    small_file = open("00" + settings_dict["project"] + "-" + "nav_menu_items" + ".txt", "w")

    # Iterate on posts, create files for the complete list and append for the small list
    for single_item in list_of_items:
        # Small file
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")
        small_file.write("--------------- \n")
        small_file.write("Title: ... " + single_item.title + "\n")
        small_file.write("Marked Title: ... " + " ".join(single_item.title_small_list) + "\n")
        # Unable to find where it used in wp site and where to edit it on wp control panel
        # small_file.write("Name: ... " + single_item.name + "\n")
        # small_file.write("Marked Name: ... " + " ".join(single_item.name_small_list) + "\n")
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")

    # Close the small file
    small_file.close()

    # Return to root folder
    return_to_root()


def folder_maker(folder_name: str):
    """
    Check if folder_name exist. If not, creates it. Note: FoLder != folder
    :param folder_name: Target folder name
    :return:
    """
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass

    # Change path to that dir
    os.chdir(folder_name)

    # Remove simple list file
    try:
        os.remove("00" + folder_name + ".txt")
    except FileNotFoundError:
        pass


def return_to_root():
    """
    Return pwd to root path
    :return: none
    """
    os.chdir("..")
    os.chdir("..")


def sort_item_type(obj_list: list, str_type: str):
    """
    Creates a new list with str_type objects.
    :param obj_list: list of item objects
    :param str_type: Output needed type
    :return: list of object containing only str_type item
    """
    by_type_list = list()
    sorted_list = list()

    for current_obj in obj_list:
        if current_obj.type == str_type:
            by_type_list.append(current_obj)

    # Sort certain object list by ABC
    if str_type == POST_TYPE or str_type == PAGE_TYPE or str_type == MEDIA_TYPE or str_type == NAV_MENU_ITEM_TYPE:
        sorted_list = sorted(by_type_list, key=lambda post: post.title)
    elif str_type == GLOSSARY_TYPE or str_type == NAV_MENU_TYPE or str_type == CATEGORY_TYPE or str_type == TAG_TYPE:
        sorted_list = sorted(by_type_list, key=lambda tag: tag.name)
    else:
        raise Exception("Unknown sorting type: " + str_type)

    return sorted_list
