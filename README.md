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
### Pages and Posts
```sql
SELECT ID,post_content,post_title,post_excerpt,post_name,guid,post_type
FROM wp_posts 
WHERE (post_type = "page" OR post_type = "post") AND post_status = "publish";
```

### Media
```sql
SELECT ID,post_content,post_title,post_excerpt,post_name,guid,post_type
FROM wp_posts 
WHERE post_type = "attachment" ;
```

### Tags and Categories
```sql
SELECT wp_terms.term_id,wp_terms.name,wp_terms.slug,wp_term_taxonomy.taxonomy,wp_term_taxonomy.description
FROM wp_terms
INNER JOIN wp_term_taxonomy ON (wp_term_taxonomy.term_id = wp_terms.term_id)
WHERE wp_term_taxonomy.taxonomy = "category" OR 
      wp_term_taxonomy.taxonomy = "post_tag" OR 
      wp_term_taxonomy.taxonomy = "nav_menu" OR 
      wp_term_taxonomy.taxonomy = "glossary-cat";
```

### Menu items
```sql
SELECT ID,post_content,post_title,post_excerpt,post_name,guid,post_type
FROM wp_posts
WHERE post_type="nav_menu_item";
```

## Python csv delimiter workaround
Python assumes that a line break means end of line in csv even if you configured something else.
As WP posts tend to have a lot of line breaks, this might be problematic. 
Therefore run __line_end.sh__ script __before__ running the program. 
The script will add a workaround to any csv file in the folder (not recursive).

## Config.txt
__Format:__ options:=value

__Don't add spaces before or after keys or values__

### Available options
* posts_csv_name: Posts and Pages file name
* media_csv_name: Media file name
* tag_csv_name: Tags and Categories file name
* nav_csv_name: Nav menu items file name
* project: Output folder name

#### How does the script mark foreign strings?
* mark_start: prefix 
* mark_end: postfix

With text output ‡‡‡‡ will produce:
```text
‡‡‡‡ Foreign ‡‡‡‡ ‡‡‡‡ text ‡‡‡‡
```

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
