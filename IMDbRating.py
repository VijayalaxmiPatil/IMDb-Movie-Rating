########################################################

# Description: This script randomly picks any number of movies specified by user and prints its details viz., title, year and summary
#######################################################


from lxml import html
import requests
import random

def moviePicker(Num_Of_Movies_To_Display):
    count = 0
    while(count < Num_Of_Movies_To_Display):
        page = requests.get('http://www.imdb.com/chart/top')
        tree = html.fromstring(page.content)
        rand = random.randint(1,50)

        title = tree.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[' + str(rand) +']/td[2]/a/text()')
        yearReleased = tree.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[' + str(rand) + ']/td[2]/span/text()')

        # Parse the movie's url and pull the summary from the details page
        movieUrl = str(tree.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[' + str(rand) + ']/td[2]/a/@href'))
        removeFront = movieUrl.replace("['", "")
        cleanUrl = 'http://www.imdb.com' + removeFront.replace("']", "")
        moviepage = requests.get(cleanUrl)
        details = html.fromstring(moviepage.content)
        movieSummary = details.xpath("normalize-space(//div[@class='summary_text']/text())")

        count = count + 1
        print(title)
        print(yearReleased)
        print( movieSummary)

Num_Of_Movies = 3
moviePicker(Num_Of_Movies)