from datetime import datetime
import pandas as pd
import httplib2
from bs4 import BeautifulSoup, SoupStrainer


dates = []
all_headlines = []
for date in list(pd.date_range(datetime(2007, 1, 1), datetime.now())):

	dates.append(date)

	str_date = date.strftime('%m%d%Y')

	http = httplib2.Http()
	status, response = http.request('http://www.reuters.com/news/archive/worldNews?date={}'.format(str_date))

	soup = BeautifulSoup(response)
	mydivs = soup.findAll('div', {'class': 'moduleBody'})[0].findAll('div', {'class': 'feature'})
	
	day_headlines = ''
	for i in range(len(mydivs)):
		day_headlines += str(mydivs[i].h2.a).split('>')[1][:-3]
		day_headlines += ' '

	all_headlines.append(day_headlines)

	if date.day == 1:
		print str_date

	if date.month ==1 and date.day ==1:
		pd.DataFrame()
		pd.DataFrame([dates, all_headlines], index = ['dates', 'headlines']).transpose().to_csv('date_headlines_{}.csv'.format(str(date.year)))


pd.DataFrame([dates, all_headlines], index = ['dates', 'headlines']).transpose().to_csv('date_headlines.csv')




