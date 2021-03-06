# wpmanualtranslation
Locates foreign strings in Worpress sites. This program doesn't access the db directly, 
instead it reads the data from csv files. Required sql queries shown bellow. 
Program should work on Windows but was not tested. The script won't work on Windows. Tested on Linux only.

__Use-cases__:

1. You want to translate a site from one language to another by copying the whole site and 
    translating all objects (pages, post, categories and so on).
2. Translating the site with plugins failed (Maybe due to conflicts with other plugins) and you need an alternative.

## SQL Queries
When saving the csv file use utf-8 encoding, † as line delimiter and ‡ as field delimiter. 
### Pages, Posts, Media and Nav Menu Items:
```sql
SELECT ID,post_content,post_title,post_excerpt,post_name,guid,post_type,post_status
FROM wp_posts 
WHERE post_type != "revision" AND post_status != "auto-draft"
```

### Tags and Categories
```sql
SELECT wp_terms.term_id,wp_terms.name,wp_terms.slug,wp_term_taxonomy.taxonomy,wp_term_taxonomy.description
FROM wp_terms
INNER JOIN wp_term_taxonomy ON (wp_term_taxonomy.term_id = wp_terms.term_id)
```

## Python csv delimiter workaround
Python assumes that a line break means end of line in csv even if you configured something else.
As WP posts tend to have a lot of line breaks, this might be problematic. 
Therefore run __line_end.sh__ script __before__ running the program. 
The script will add a workaround to any csv file in the folder (not recursive).

## Config.txt
__Format:__ options:=value

__Don't add spaces before or after or inside keys or values__

__Don't use colons ":" or equal signs "=" inside keys or values__

### Available options
* posts_csv_name: Posts and Pages file name
* tag_csv_name: Tags and Categories file name
* project: Output folder name
* language: Required language. Use 2 chars code from https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes, column 639-1
* image: Custom string to replace image tags (for context)
* h5p: Custom string to replace h5p tags (for context)

#### How does the script mark foreign strings?
* mark_start: prefix 
* mark_end: postfix

With text output ‡‡‡‡ will produce:
```text
‡‡‡‡ Foreign text ‡‡‡‡
```

## Language Support
Theoretically speaking, wpmanualtranslation support all languages. 
However, it depends on guess_language which has it own supported languages plus those enchant supports.

__Due to wpmanualtranslation implementation, you'll need to add languages manually to setting.py's lang_to_system function:__
lang_to_system function allows wpmanualtranslation to build sentences written in one language. 
Why? Because guess_language returns better results the longer the string is. 
What do I need to do?
1. Prepare one char that belongs to the new site target language's writing system: https://simple.wikipedia.org/wiki/Writing_system
2. Open python interactive shell
3. Run ```python from unicodedata import name as writing_system```
4. Change <char> to the one you prepared in 1: ```python writing_system("<char>").split()[0]``` (DO NOT remove the enclosing "").
5. Run that line in the interactive shell.
6. Copy the output and add a new elif for it or expand existing (Use the language code from config.txt)

#### Example for Spanish 
1. I chose "ñ".
2. To open a shell on my system, I opened a Terminal and entered "python3" and Enter.
3. Pasted the line. 
4. My cmd is: writing_system("ñ").split()[0]
5. Run it and got 'LATIN'
6. When I open settings.py, I see that's LATIN is already there:
```python
    elif str_lang == "en" or str_lang == "fr":
        return "LATIN"
```
7. All I need to do is to add another "or" for "es" (Spanish lang code):
```python
    elif str_lang == "en" or str_lang == "fr" or str_lang == "es":
        return "LATIN"
```
8. That's it, now wpmanualtranslation supports Spanish.

## Wordpress plugin support
1. CM Tooltip Glossary
2. Contact Form 7

To add support for new plugins (Only needed if they use new post or tag type):

Just search for a supported plugin in the code (like CM_TOOLTIP_GLOSSARY_TYPE) and yours.

## Project structure
1. settings.py: Reads the settings from config.txt
2. csvparser.py: Parses the csv files and creates item lists (Calls the proper class constructor).
3. htmlparser.py: Remove unneeded html tags from the content. Replaces images with \*\*\*\*Image\*\*\*\*.  
4. baseitem.py: Parent class for items.
5. post.py, tag.py: Classes for each item type (post also accommodates pages, media and nav items, 
tag also accommodates categories and menu items).
6. foreign.py: Detects foreign strings.
7. outputcreator.py: Creates the output files. small file vs complete file: 
    small file contains only the foreign strings, complete contains everything. Use complete for context. 
8. main.py: Main

## Required libs
1. Python 3.8+
2. PyEnchant (For better results). Requires the enchant package installed on your OS.
3. guess_language: https://bitbucket.org/spirit/guess_language/src/default/

## Known bugs
1. Complete list is not so complete as it doesn't include non foreign strings. I'll fix it in the future. 
Low priority as it used only for debug. 
