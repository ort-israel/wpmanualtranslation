def read_settings():
    """Read settings from the config file and returns the setting as dictionary
    List of possible settings:
    csv_name: csv file name
    db_user: db username
    db_pass: db password
    db_port: db port
    db_link: db link
    mark_start: Mark start
    mark_end: Mark end
    project: Project name. Will be used as output folder name and small file name
    """

    settings_dict = dict()

    with open("config.txt") as settings_file:
        for line in settings_file:
            if not(line.startswith("#")) and not(line == ""):
                # Remove end of line char
                line = line.strip("\n")

                # Splitting on :=
                key, value = line.split(":=")
                settings_dict[key] = value

    return settings_dict


