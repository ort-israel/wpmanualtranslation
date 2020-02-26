# wpmanualtranslation

## Project structure
1. db.py: Gets the post data from the db. It then convert each table to array. Or maybe use CSV and load it to arrays?|
https://github.com/mkleehammer/pyodbc
2. html.py: Breaks each post to segments by div and p tags (or whatever else in there) **** >>>>>> Check the code
Should I create a class for each post? 
3. foreign.py: Checks each post segment and tag their language. 
4. export2csv.py: export all segments to csv

** Line delimiter is † **  

** Field separator is ‡ ** 

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
1. [ ] Output should not include objects that don't need translation. Implemented - Check if working after no. 3.
2. [x] Rest of the hardcoded settings ("ar")
3. [ ] Foreign should not add "empty" strings to complete and small list (aka "\r", "\r\n", "\t" "  "). <=== Check if working
4. [x] License: http://www.gnu.org/licenses/gpl-howto.html  (The license notices)
5. [ ] Tags: Separate for tags, categories, menu items and customized links (add object var for type)
6. [ ] Posts: Add object var for type and than drop name marking for nav_menu_item

## For v0.4
1. [ ] Convert pages and post to use inheritance.
2. [ ] foreign requires string (due to python csv bypass) but htmlparser (due to my implementation) returns list.
    Refactor htmlparser 
3. [ ] Print output to csv
4. [ ] Sort by ABC of the original language (small list only)
5. [ ] Complete list doesn't include non foreign string. Why? 

## For 0.5
1. [ ] media.py is not used. Should it be used or just delete it? (Media and Post have the same fields)
2. [ ] h5p?
3. [ ] Print output to html
4. [ ] WP Plugin: CM Tooltip Glossary. Saved under wp_posts as type glossary
5. [ ] WP Plugin: Contact Forms with contact form 7. Saved under wp_posts as type wpcf7_contact_form

## For 0.6 
1. [ ] Check that all required settings are in the file. If settings are missing or unknown setting were entered, use raise