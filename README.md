# foxymoron
pulls date, url, and title from firefox's places.sqlite

put your places.sqlite file in the same folder as foxymoron.py
./foxymoron.py

History will be displayed


TODO:
    pass sqlite filename as arg
    pull urls last visited between dates
    grab cookies and downloads history as well
    fix weird bugs
    migrate to more object oriented/pythonic coding style 
    
Notes:
    Counter is how many times the exception is thrown in the try-except block.  Still need to figure out what exactly is throwing that when converting title to string (tried decoding/encoding ascii/utf-8 with no success)
