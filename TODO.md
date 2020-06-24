## For v0.1
0. [x] Read Settings file. settings.py. V function was written
1. [x] Get posts from csv. csv.py for parsing csv, post.py - post class - for each post. post.py is done V
2. [x] Check post lang. Assume Hebrew is needed. Returns one list with all text and hebrew marked and one with just hebrew foreign.py V
3. [x] Print to csv file: page link and number of foreign words detected. Runs foreign.py on each post class. Part of main. V

## For v0.2
1. [x] Excerpt - Done, pages (Same as posts) - Done, media (uses post class), tags (Done)
    When classes are done add print to the outputcreator.py
    Maybe post_type = "nav_menu_item" in wp_posts? Check if working - Done
2. [x] Why arabic is not recognised? Maybe use this: 
    https://stackoverflow.com/questions/42510056/detect-the-writing-system-of-a-string-in-python/42510267 Done
3. [x] Settings: Done
4. [x] Maybe Mark string in the name too (for Post and base item)? Done
5. [x] Translate string like %d7%91%d7%97%d7%9f-%d7%90%d7%aa to something readable - https://www.url-encode-decode.com/
urllib.parse.unquote("String") from https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote Done

## For v0.3
1. [x] Output should not include objects that don't need translation. Redo after type was added
2. [x] Rest of the hardcoded settings ("ar")
3. [x] Foreign should not add "empty" strings to complete and small list (aka "\r", "\r\n", "\t" "  ").
4. [x] License: http://www.gnu.org/licenses/gpl-howto.html  (The license notices)
5. [x] Add type to sql queries and to base item
6. [x] Convert pages and post to use inheritance.
7. [x] Tags: Separate output for tags, categories, menu items and customized links
8. [x] Posts: Separate output for pages and posts

## For v0.4
1. [x] Posts: drop name marking for nav_menu_item
2. [x] Foreign requires string (due to python csv bypass) but htmlpalrser (due to my implementation) returns list.
    Refactor htmlparser 
3. [x] Sort non content or excerpt fields by ABC of the original language (small list only)  
4. [x] media.py is not used. Should it be used or just delete it? (Media and Post have the same fields). Deleted
5. [x] Use settings dict where needed instead of passing vars to functions

## For 0.5
1. [x] Check that all required settings are in the file. If settings are missing or unknown setting were entered, use raise
Complete the init of setting_dict in the beginning of settings.py and than add if to make sure no "Def" remain.
2. [x] Lower the number of sql queries to 2: tag table and post table. Required for plugins.
3. [x] Brainstorm and get feedback for output formatting: Table. Add link and id. 
Use pyexcel? Don't use csv to xls/ods if I can't set the delimiters (content has a lot of , or tabs)
4. [x] Add plugin support: https://alysivji.github.io/simple-plugin-system.html and last one here: 
https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string
5. [x] WP Plugin: CM Tooltip Glossary. Saved under wp_posts as type glossary. Does glossary-cat from tags table belong to it?
If so, add it to this plugin. Post type: glossary
6. [x] WP Plugin: Contact Forms with contact form 7. Saved under wp_posts as type wpcf7_contact_form.
7. [x] post.is_post_translation_needed(): Was created to speedup the program but causes plugins to get empty lists (Because those item types are declared
inside the plugin and not in the main program). Need to find a solution and re-test the plugins
8. [x] Plugins made my life harder. Reverting to no plugin architecture.

## For 0.6
Bugs: [x] Media folder is empty. Why? Maybe the change in the query? Yes. Fixed it in Heidi. Now update the readme and the files.
1. [ ] In output creator: Merge nav menu items and tags. Use if for specific stuff
2. [ ] Rewrite content_lang_marker so it'll get a string instead of list. post, tag and baseitem are ready.
3. [ ] Complete list doesn't include non foreign string. Need to split content_lang_marker. 
Sentence building drops non foreign strings. Maybe add a complete list in the first if (is_word_system_bad)
4. [ ] Strip lines of non printable chars before printing as a table.
5. [ ] Print output to word as table. By post title or tag name

## For 0.7
1. [ ] GUI?
2. [ ] Ability to ignore items (So they won't show in the output)
3. [ ] h5p?
4. [ ] Absolute paths in output creator
5. [ ] Change to package architecture for better pythonist code in plugins
6. [ ] Add function that deletes settings["project"] folder if it already exists in the beginning of exec.
