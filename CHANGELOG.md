# v0.1 First Release \ Proof of Concept
1. Support for post content only
2. Settings are hardcoded, except csv file name (Minimal implementation so I'll know it working).
3. Output is text only. Marking is ‡‡‡‡ __string__ ‡‡‡‡
4. Inline marking of h5p and image object by \*\*\*\* Image\h5p \*\*\*\*

# v0.2
1. Less hardcoded settings: string marking, output folder name. 
2. Excerpt support
3. Media, Pages and tags.
4. Redesign: Base class for item storage. Tags and Media inherit it. Post and pages in the future.
5. Nav menu item support
6. Marking for name and title (Post, media and tags)
7. README organized. TODO stuff moved from README to TODO. 
8. URL decode support for item name field.
9. Rewrite of foreign detection functions for better detection. 

# v0.3 
1. Output no longer includes items that don't need translation.
2. Spaces and non printable (such as "\n" and "\r") no longer marked for translation
3. Inheritance implemented for post item type.
4. Added type var for items.
5. Added GPL license notification.
6. All of the hardcoded settings are now configurable. 

# v0.4
1. Nav menu item name field is no longer scanned for foreign language. 
It appears that it's no longer possible to edit this field in Wordpress GUI so why scan it?
2. htmlparser returns a string instated of list (Simplifying the code)
3. Outpust is now sorted by ABC. For Post and Pages: Title is used.
4. Removed media.py file as it's not used.
5. Settings are no longer passed as function parameters as the settings dictionary is imported by every file.   