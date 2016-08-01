#!/usr/bin/env python
import sqlite3

dbconnect = sqlite3.connect('./places.sqlite')
dbcurs = dbconnect.cursor()
dbcurs.execute("SELECT datetime(last_visit_date/1000000,'unixepoch') AS Time, url, title FROM moz_places ORDER BY Time ASC;")
counter = 0
for rows in dbcurs:
    itemDate = str(rows[0])
    itemURL = str(rows[1])
    try:
        itemTitle = str(rows[2])
        if itemTitle is not None:
            unicodeItemTitle = itemTitle

        else:
             unicodeItemTitle = "no title"
        if itemDate is None:
            itemDate = "no date"
        if itemURL is None:
            itemURL = "no url"
        
        print '[+] ' + itemDate + ' - Visited: ' + itemURL + '- Title: ' + unicodeItemTitle
        print '\n' 
    except:
       
        print '\n'
        print '[+] ' + itemDate + ' - Visited: ' + itemURL + '- Title: ' + 'Unknown'
        
        counter = counter + 1

print counter
dbconnect.close()
