#!/bin/bash
#    <Simple tool to manually find string that need to be translated in a wordpress for cases where you chose to duplicate the site>
#    Copyright (C) <2020>  <Shay Gover, ort-israel>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Goes around the "The reader is hard-coded to recognise either '\r' or '\n' as end-of-line, and ignores lineterminator. This behavior may change in the future." https://docs.python.org/3/library/csv.html
# Line delimiter is † 
# Field separator is ‡
# First I'll change \r to ř . Then \n to ň
# Thanks to http://www.fileformat.info/info/charset/UTF-8/list.htm
# The python script will have to **reverse** that (in the csv reader)
# Finaly † is turned back into \r\n
# Why a simple replacement for \n won't work https://stackoverflow.com/questions/1251999/how-can-i-replace-a-newline-n-using-sed
for file in $(ls -1 | grep .csv); do
    sed -i 's,\r,ř,g' $file
    sed -i ':a;N;$!ba;s/\n/ň/g' $file
    sed -i 's,†,\r\n,g' $file
done
