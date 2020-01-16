import post
import os


def text_output(list_of_posts: list, folder_name: str):
    """
    Prints the results to files.
    Small list goes into a single file with ********** separator between posts. File name is 00<folder_name>
    Complete list: Each post gets it's own file
    :param list_of_posts: All the posts
    :param folder_name: Folder to save the files in.
    :return:
    """
    # Check the folder exists
    # Open the small list file for writing and clear it
    folder_maker(folder_name)
    small_file = open("00"+folder_name+".txt", "w")

    # Iterate on posts, create files for the complete list and append for the small list
    for single_post in list_of_posts:
        # Complete list
        complete_file = open(single_post.title + ".txt", "w")
        complete_file.write("--------------------------------------------------------------------------------- \n")
        complete_file.write("Post Title: ... " + single_post.title + "\n")
        complete_file.write("Post Name: ... " + single_post.name + "\n")
        complete_file.write("Post Link: ... " + single_post.link + "\n")
        complete_file.write("--------------------------------------------------------------------------------- \n \n")
        complete_file.write("Post Excerpt: \n")
        complete_file.write(" ".join(single_post.excerpt_complete_list))
        complete_file.write("--------------------------------------------------------------------------------- \n \n")
        complete_file.write(" ".join(single_post.content_complete_list))

        # Close the complete file
        complete_file.close()

        # Small file
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")
        small_file.write("--------------- \n")
        small_file.write("Post Title: ... " + single_post.title + "\n")
        small_file.write("Post Name: ... " + single_post.name + "\n")
        small_file.write("Post Link: ... " + single_post.link + "\n")
        small_file.write("Post Excerpt: ... " + " ".join(single_post.excerpt_small_list) + "\n")
        small_file.write("--------------- \n \n")
        small_file.write(" ".join(single_post.content_small_list) + "\n")
        small_file.write("************************************************************************************ \n")
        small_file.write("************************************************************************************ \n")

    # Close the small file
    small_file.close()


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
    # else:
        # print("Fatal error creating the folder")

    # Change path to that dire
    os.chdir(folder_name)

    # Remove simple list file
    try:
        os.remove("00"+folder_name)
    except FileNotFoundError:
        pass
