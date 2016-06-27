#Markov Webscraper
#!/usr/bin/env python -tt
  
import urllib2
from lxml.html import fromstring
import sys
import time
  
urlprefix = "http://www.ratebeer.com/beer-ratings/0/"
f = open("Beer_2.txt", "w")

#100
for page in xrange(0, 99):
    try:
        out = "-> On page {} of {}....      {}%"
        print out.format(page, "100", str(round(float(page)/100*100, 2)))
        response = urllib2.urlopen(urlprefix + str(page)+'/')
        html = response.read()
        dom = fromstring(html)
        for i in xrange(1,15):
            xpathprefix = '//*[@id="rbbody"]/div[4]/div/div/div[1]/table/tbody/tr['
            xpathsuffix = ']/td[2]/div/text()[1]'
            current = xpathprefix + str(i)+xpathsuffix
            sels = dom.xpath(current)
            rev= ''.join(sels)
            if rev:
                f.write(rev)
                f.flush()
            sys.stdout.flush()
            time.sleep(2)
    except:
        continue
# capture output of script
f.close
##//*[@id="rbbody"]/div[4]/div/div/div[1]/table/tbody/tr[2]/td[2]/div/text()
##//*[@id="rbbody"]/div[4]/div/div/div[1]/table/tbody/tr[3]/td[2]/div/text()[1]
##//*[@id="rbbody"]/div[4]d/iv/div/div[1]/table/tbody/tr[15]/td[2]/div/text()
