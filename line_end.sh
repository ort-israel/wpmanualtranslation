# Goes around the "The reader is hard-coded to recognise either '\r' or '\n' as end-of-line, and ignores lineterminator. This behavior may change in the future." https://docs.python.org/3/library/csv.html
# Line delimeter is † 
# Field seperator is ‡
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
