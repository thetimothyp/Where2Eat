from flask import Flask, render_template
import random
from yelp import *

#GOOGLE SEARCH
# def showsome(searchfor):
# 	query = urllib.parse.urlencode({'q': searchfor})
# 	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
# 	search_response = urllib.request.urlopen(url)
# 	search_results = search_response.read().decode("utf8")
# 	results = json.loads(search_results)
# 	data = results['responseData']
# 	if(data):
# 		hits = data['results']
# 		return hits[0]['url']
# 	return ''


app = Flask(__name__)


@app.route("/")


def template_test():
	yelp = False
	results=search_yelp("irvine")
	restaurants=results[0]
	urls=results[1]
	i=random.randint(0,len(restaurants)-1)
	# result=search_yelp(restaurants[i],"irvine")
	return render_template('template.html', search_result=urls[i], rand_int=i, my_list=restaurants)

if __name__ == '__main__':
	app.run(debug=True)
