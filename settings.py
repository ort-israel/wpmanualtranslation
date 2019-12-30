def read_settings():
    """Read settings from the config file and returns the setting as dictionary"""

    settings_dict = dict()

    with open("config.txt") as settings_file:
        for line in settings_file:
            if not(line.startswith("#")) and not(line == ""):
                # Remove end of line char
                line = line.strip("\n")

                # Splitting on :=
                key, value = line.strip(":=")

    return settings_dict


