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
