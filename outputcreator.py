import post
import os


def tag_text_output(list_of_tags: list, folder_name: str, str_type="Tags"):
    """

    :param str_type: Subdirectory name. Should be tags
    :param list_of_tags: All the tags to print.
    :param folder_name: Project name
    :return:
    """
    # Check the folder exists
    # Open the small list file for writing and clear it
    folder_maker(folder_name)
    folder_maker(str_type)
    small_file = open("00" + folder_name + "-" + str_type + ".txt", "w")

    # Iterate on tags, create files for the complete list and append for the small list
    for single_item in list_of_tags:
        # Complete list
        complete_file = open(single_item.name + ".txt", "w")
        complete_file.write("--------------------------------------------------------------------------------- \n")
        complete_file.write("Name: ... " + single_item.name + "\n")
        complete_file.write("Marked Name: ... " + " ".join(single_item.name_complete_list) + "\n")
        complete_file.write("Type: ... " + single_item.type + "\n")
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
        small_file.write("Type: ... " + single_item.type + "\n")
        small_file.write("--------------- \n \n")
        small_file.write(" ".join(single_item.desc_small_list) + "\n")
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")

    # Close the small file
    small_file.close()

    # Return to root folder
    return_to_root()


def post_text_output(list_of_items: list, folder_name: str, str_type: str):
    """
    Prints the results to files.
    Small list goes into a single file with ********** separator between posts. File name is 00<folder_name>
    Complete list: Each post gets it's own file
    :param str_type: Type of items: Posts and pages or Media
    :param list_of_items: All the posts
    :param folder_name: Folder to save the files in.
    :return:
    """
    # Check the folder exists
    # Open the small list file for writing and clear it
    folder_maker(folder_name)
    folder_maker(str_type)
    small_file = open("00" + folder_name + "-" + str_type + ".txt", "w")

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


def nav_text_output(list_of_items: list, folder_name: str):
    """
    Prints the menu items to a single file (Only item name, title and id are relevant)
    :param list_of_items: list of menu item. Type is post class
    :param folder_name: Project name
    :return: Prints everything to a file called nav_menu_items.txt
    """
    # Check the folder exists
    # Open the small list file for writing and clear it
    folder_maker(folder_name)
    small_file = open("00" + folder_name + "-" + "nav_menu_items" + ".txt", "w")

    # Iterate on posts, create files for the complete list and append for the small list
    for single_item in list_of_items:
        # Small file
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")
        small_file.write("--------------- \n")
        small_file.write("Title: ... " + single_item.title + "\n")
        small_file.write("Marked Title: ... " + " ".join(single_item.title_small_list) + "\n")
        small_file.write("Name: ... " + single_item.name + "\n")
        small_file.write("Marked Name: ... " + " ".join(single_item.name_small_list) + "\n")
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
