# wpmanualtranslation

## Project structure
1. db.py: Gets the post data from the db. It then convert each table to array. Or maybe use CSV and load it to arrays?|
https://github.com/mkleehammer/pyodbc
2. html.py: Breaks each post to segments by div and p tags (or whatever else in there) **** >>>>>> Check the code
Should I create a class for each post? 
3. foreign.py: Checks each post segment and tag their language. 
4. export2csv.py: export all segments to csv

## For v0.1
0. Read Settings file. settings.py. V function was written
1. Get posts from csv. csv.py for parsing csv, post.py - post class - for each post. post.py is done
2. Check post lang. foreign.py
3. Print to csv file: page link and number of foreign words detected. Runs foreign.py on each post class.