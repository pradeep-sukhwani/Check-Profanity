import urllib

def read_txt():
    quotes = open("C:\Python27\My-File\movie_quotes.txt")
    contents_of_file = quotes.read()
    print contents_of_file
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen ("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    #print output
    connection.close()
    if "true" in output:
        print "Profanity Alert!!"
    elif "false" in output:
        print "This document has no curse words!"
    else:
        print "I couldn't scan the document."

read_txt()
