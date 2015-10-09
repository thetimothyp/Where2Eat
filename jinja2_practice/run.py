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
	restaurants=["Fukada 2 Go", "Alberto\'s", "Ruby\'s Diner", "Costco", "Pho", "Taco Co.", "Islands", "Kicking Crab", "Ramen Yamadaya", "Super Mex", "Red Robin", "Boiling Point", "Thai Spice", "Le Dip", "Panda Express", "BWW", "Mick\'s", "Cali Fish Grill", "Wholesome Choice", "Wingstop", "The Habit", "Bear Flag", "Gatten Sushi", "Suplantation", "McDonalds", "Chick-Fil-A", "Sake 2 Me", "Cali Tacos", "In-n-Out", "Subway", "KBBQ", "Thai and Chinese Express", "Taco Bell", "Flame Broiler", "Pizza Hut", "Annapoorna", "Aloha", "Ajisen", "Blaze", "Tang 190", "Baja Fresh", "Carl\'s Jr.", "Jack-in-the-Box", "Yardhouse", "Coco Ichibanya", "Banh Mi", "Jollibee", "Sam Woo", "Albertson\'s", "El Pollo Loco", "Arby\'s", "Seaside", "Eureka", "Gen", "Kogi", "Pieology", "Koba", "BCD", "Chipotle", "Domino\'s", "Farm Direct", "Tokyo Table", "Togo\'s", "Quizno\'s", "Mitsuwa", "The Counter", "Bruxie\'s", "Lazy Dog", "101 Noodle Express", "Stonefire Grill", "Urban Seoul", "Sonic", "Din Thai Fung", "Lemonade", "Class 302", "Native Foods"]
	i=random.randint(0,len(restaurants)-1)
	result=search_yelp(restaurants[i],"irvine")
	return render_template('template.html', search_result=result, rand_int=i, my_list=restaurants)

if __name__ == '__main__':
	app.run(debug=True)
