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

### input: array keys, string val
### output: array 
def getTweetsByAttributes(tweets, keys, val):
	filtered = []
	for attribute in tweets:
		original = attribute;
		for key in keys:
			attribute = attribute[key]
			if not attribute:
				break
		if attribute.lower() == val.lower():
			filtered.append(original)
	return filtered

### input: array keys
### output: array 
def getUniqueValues(tweets, keys):
	values = []
	for attribute in tweets:
		original = attribute;
		for key in keys:
			attribute = attribute[key]
			if not attribute:
				break
		values.append(attribute)
	values = set(values)
	return values
