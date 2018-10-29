import json
	
### output: array
def getTweets():
	tweets = []
	with open("p2000a.txt", "r") as f:
		lines = f.readlines()
		for line in lines:
			tweets.append(json.loads(line))
	with open("p2000b.txt", "r") as f:
		lines = f.readlines()
		for line in lines:
			tweets.append(json.loads(line))
	return tweets

### input: array tweets, array keys, string val
### output: array 
def getTweetsByAttributes(tweets, keys, val):
	filtered = []
	for attribute in tweets:
		original = attribute;
		for key in keys:
			try: 
				attribute = attribute[key]
			except KeyError:
				break
		if type(attribute) == "string" and attribute.lower() == val.lower():
			filtered.append(original)
	return filtered

### input: array tweets, array keys
### output: array 
def getUniqueValues(tweets, keys):
	values = []
	for attribute in tweets:
		original = attribute;
		for key in keys:
			try: 
				attribute = attribute[key]
			except KeyError:
				break
		if type(attribute) == "string":
			values.append(attribute)
	values = set(values)
	return values