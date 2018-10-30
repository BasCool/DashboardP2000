import json

### output: string
def getTweetsString():
	tweets = None
	with open("p2000a.txt", "r") as f:
		tweets = f.read()
	with open("p2000b.txt", "r") as f:
		tweets = tweets + "\n" + f.read()
	return tweets
	
### output: array
def getTweetsArray():
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
		found = True
		for key in keys:
			try: 
				attribute = attribute[key]
			except (KeyError, IndexError):
				found = False
				break
		if found and attribute == val: 
			filtered.append(original)
	return filtered

### input: array tweets, array keys, string substring
### output: array 
def getTweetsByAttributesWithFind(tweets, keys, substring):
	filtered = []
	for attribute in tweets:
		original = attribute;
		found = True
		for key in keys:
			try: 
				attribute = attribute[key]
			except (KeyError, IndexError):
				found = False
				break
		if found and not attribute.find(substring) == -1: 
			filtered.append(original)
	return filtered

### input: array tweets, array keys
### output: array 
def getUniqueValues(tweets, keys):
	values = []
	for attribute in tweets:
		original = attribute;
		found = True
		for key in keys:
			try: 
				attribute = attribute[key]
			except (KeyError, IndexError):
				found = False
				break
		if found:
			values.append(attribute)
	values = set(values)
	return values
