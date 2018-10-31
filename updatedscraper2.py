

import urllib.request
import urllib.error
import csv
from bs4 import BeautifulSoup

n= 0 ## set the loop variable to 0

commence_id = 100817   ##starting id of website document

url = 'http://www.margaretthatcher.org/document/'  ##base structure of all URLs

while n < 100:  ##define scope of loop

    usable_url = url + str(commence_id)  ##append first id to base url and convert to string

    new_number = commence_id + 1 ##increase url id by

    new_url = url + str(new_number) ##convert to string

    print(new_url)  ##print - error handling

    commence_id = new_number   ##update commence id for next iteration

    response = urllib.request.urlopen(new_url)  ##open up URL

    html = response.read() ## grab the HTML

    soupit = BeautifulSoup(html)   ##convert HTML to Beautiful Soup Object

    check = soupit.body['class']  ##grab HTML type by class tag

    if check == 'speeches c2':
        print("correct")       ## check if HTML is a speech

        title = soupit.title

        print(title)

        classed = str(soupit('p'))  ## pull everything in HTML in <p> tags

        text_file=open("thatcher_data_1000", "a")  ##create text file to hold data. Note "a" parameter to enable appending of data not overwriting

        text_file.write(classed)   ##write <p> tags to text file

        text_file.close()  ##close down text file

        n+=1
    else:
        print("incorrect type")

        n+=1
