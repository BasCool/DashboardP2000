import json

Tweets = []
	
### output: array
def getTweets():
	with open("p2000a.txt", "r") as f:
		lines = f.readlines()
		for line in lines:
			Tweets.append(json.loads(line))
	with open("p2000b.txt", "r") as f:
		lines = f.readlines()
		for line in lines:
			Tweets.append(json.loads(line))

### input: array keys, string val
### output: array 
def getTweetsByAttributes(keys, val):
	tweets = []
	for attribute in Tweets:
		original = attribute;
		for key in keys:
			attribute = attribute[key]
			if not attribute:
				break
		if attribute.lower() == val.lower():
			tweets.append(original)
	return tweets

### input: array keys
### output: array 
def getUniqueValues(keys):
	values = []
	for attribute in Tweets:
		original = attribute;
		for key in keys:
			attribute = attribute[key]
			if not attribute:
				break
		values.append(attribute)
	values = set(values)
	return values

getTweets()
