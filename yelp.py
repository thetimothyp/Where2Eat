import json
import rauth

def get_search_parameters(name, location):
	params = {}
	params["term"] = "{}".format(name)
	params["location"] = "{}".format(location)
	params["radius_filter"] = "2000"
	params["limit"] = "1"
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

def search_yelp(name,location):
	queries = [(name,location)]
	api_calls = []
	for name,location in queries:
		params = get_search_parameters(name,location)
		api_calls.append(get_results(params))
	for item in api_calls:
		return item['businesses'][0]['url']