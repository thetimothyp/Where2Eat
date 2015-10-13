from flask import Flask, render_template, request
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

# Results view that displays the randomly selected restaurant and the yelp link.
# If refreshed, will produce a new restaurant in the same location that was given in
# the previous view.
@app.route("/result", methods = ['POST', 'GET'])

def get_location():
        results=search_yelp(request.form['location'])
        restaurants=results[0]
        urls=results[1]
        i=random.randint(0,len(restaurants)-1)
        return render_template('restaurant.html', search_result = urls[i], my_list = restaurants, rand_int = i)

# Inital view that displays a simple page asking for a location
# Once button is clicked, user is redirected to the result view
@app.route("/", methods = ['POST', 'GET'])

def template_test():
	return render_template('template.html')

if __name__ == '__main__':
	app.run(debug=True)
