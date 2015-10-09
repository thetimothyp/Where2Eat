import json
import rauth
import time

def get_search_parameters(location,offset):
	params = {}
	params["term"] = "restaurant"
	params["offset"] = "{}".format(str(offset))
	params["location"] = "{}".format(location)
	params["radius_filter"] = "2000"
	params["limit"] = "20"
	return params

def get_results(params):
	consumer_key = "7RUTKX5es62WOntKA21eIQ"
	consumer_secret = "DQwFZ0jnvbvOyXW66YtDDzbIDaE"
	token = "fnplPbdXdEqfGQUWIVNErZoZvd6cIAZX"
	token_secret = "5CZ7HEqx7O3xbSeqducRpwKDTIE"

	session = rauth.OAuth1Session(
		consumer_key = consumer_key,
		consumer_secret = consumer_secret,
		access_token = token,
		access_token_secret = token_secret)

	request = session.get("http://api.yelp.com/v2/search", params=params)
	data = request.json()
	session.close()

	return data

def search_yelp(location):
	locations=["irvine"]
	api_calls = []
	results = []
	names = []
	urls = []
	for location in locations:
		for i in range(0,2):
			params = get_search_parameters(location,20*i)
			api_calls.append(get_results(params))
			time.sleep(1.0)
	for item in api_calls:
		results.append(item)
	for item in results:
		for i in item['businesses']:
			names.append(i['name'])
			urls.append(i['url'])
	return (names,urls)