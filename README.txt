# findQuoted
This script can be used to get certain links off webpages, or more generally, it can go through
text files, find quoted subsections, and then search those subsections for a piece of text, and if
that text appears the whole quoted section is added to a list.

## arguments
The data to be searched is entered via stdin so you can do that any way you like, including using
wget or just from files or also you can concatenate mulitple files and it will work etc.

the only commandline argument is the string to be searched for.

example usage:
``` cat testData.txt | python findQuoted.py > output.txt ```


have fun
