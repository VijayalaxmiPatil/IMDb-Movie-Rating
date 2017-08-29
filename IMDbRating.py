import sys
import re
from urllib.parse import urlparse

#The python libraries 
from mechanize import Browser
from BeautifulSoup import BeautifulSoup as bs

class ImdbRating:
	title = rating = flag = None
	BASE_url = "http://www.imdb.com"
	
	def __init__(self,title):
		self.title = title
		self._process()

	def _process(self):
		br = Browser()
		url = "%s/find?s=tt&q=%s" %(self.BASE_url,self.title)
		br.open(url)
		link = br.find_link(url_regex = re.compile(r'/title/tt*'))
		result = br.follow_link(link)
		self.url = urlparse.urljoin(self.BASE_url,link.url)
		soup = bs(result.read())


		try:
			#scrape the title
			"***"
			head = soup.find('h1').contents[1]
			if head.has_key('itemprop') and head['itemprop'] == 'name':
				self.title = head.contents[0]
			#scrape the rating
			for span in soup.findAll('span'):
				if span.has_key('itemprop') and span['itemprop'] == 'ratingValue':
					self.rating = span.contents[0]
					break
				self.flag = True

		except:
			print ("Movie not Found!!")
				

	
if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Usage: %s < Movie title required>" %(sys.argv[0]))
	else:
		Movie_Title = ''.join(sys.argv[1::])
		res = ImdbRating(Movie_Title)
		if res.flag is True:
			print("Movie : %s" %res.title)
			print("Rating: %s" %res.rating)
	
								


		


