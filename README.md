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
0. Read Settings file. settings.py. V function was written
1. Get posts from csv. csv.py for parsing csv, post.py - post class - for each post. post.py is done V
2. Check post lang. Assume Hebrew is needed. Returns one list with all text and hebrew marked and one with just hebrew foreign.py <=====
3. Print to csv file: page link and number of foreign words detected. Runs foreign.py on each post class. Part of main. 

## For v0.2
1. Excerpt - Done, pages (Same as posts) - Done, media (Class missing), tags (class is Done) and h5p (Class missing). <=======
    When classes are done add print to the outputcreator.py
    Maybe post_type = "nav_menu_item" in wp_posts?
2. Why \*\*\*\*Image\*\*\*\* Disappears after guess lang? on short list only
3. Why arabic is not recognised? Maybe use this: Should ask Moshe - Sent mail. Waiting for answer 
    https://stackoverflow.com/questions/42510056/detect-the-writing-system-of-a-string-in-python/42510267
4. Settings: Done
