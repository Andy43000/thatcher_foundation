#Python v2.6.2
#WORKINPROGRESS
#PRETTYTABLE OPTIONS AND WRITING TO TEXT PROVISIONAL
import csv 
import urllib2
import re
from BeautifulSoup import BeautifulSoup
from textblob import TextBlob
from prettytable import PrettyTable



urls = ('http://www.margaretthatcher.org/document/102487', 'http://www.margaretthatcher.org/document/102488', 'http://www.margaretthatcher.org/document/102489')

for url in urls:
    response = urllib2.urlopen(url)
    html = response.read()

    poutput = BeautifulSoup(html)

    classed = poutput('p')

    print classed

    classed2 = str(poutput)

    

    text_file = open("Output.txt", "w")

    text_file.write(classed2)

    text_file.close()

    n = 5
    
    while n == 5:
            
            with open ("C:/Python27/output.txt", "r") as myfile:
                     data=myfile.read().replace('\n', '')


                     survey = TextBlob(data)

                     a = "the"

                     a1 = survey.word_counts[a]

                     a2 = a

                     x = PrettyTable(["Phrase", "Frequency"])
                     x.add_row([a, a1])

                     n = (n +1)

                     print x

