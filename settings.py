settings_dict = dict()


def lang_to_system(str_lang: str) -> str:
    """
    Converts language to writing system
    :param str_lang: Target new site language
    :return: Writing system of str_lang
    """
    # Use writing_system("<char>").split()[0] to add new languages
    if str_lang == "he":
        return "HEBREW"
    elif str_lang == "en" or str_lang == "fr":
        return "LATIN"
    elif str_lang == "ar":
        return "ARABIC"
    else:
        raise Exception("Unknown language")


def read_settings():
    """Read settings from the config file and populates settings_dict
    List of possible settings:
    posts_csv_name: post and pages csv file name
    media_csv_name: media csv file name
    tag_csv_name: Tags and categories file name
    nav_csv_name: Nav menu items file name
    mark_start: Mark start
    mark_end: Mark end
    project: Project name. Will be used as output folder name and small file name
    language: Language needed
    """

    with open("config.txt") as settings_file:
        for line in settings_file:
            if not(line.startswith("#")) and not(line == ""):
                # Remove end of line char
                line = line.strip("\n")

                # Splitting on :=
                key, value = line.split(":=")
                settings_dict[key] = value

    # Set writing system
    settings_dict["writing_system"] = lang_to_system(settings_dict["language"])
