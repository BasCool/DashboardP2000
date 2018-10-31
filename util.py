import json
import time

priorities = [
	["A1", "P 1", "Prio: 1", "PRIO 1", "Prio 1"],
	["A2", "P 2", "Prio: 2", "PRIO 2", "Prio 2"],
	["A3", "P 3", "Prio: 3", "PRIO 3", "Prio 3"]
]

### input: string date
### output: double
### example: getUnixFromDate("Wed Sep 18 20:17:17 +0000 2013")
def getUnixFromDate(date):
	return time.mktime(time.strptime(date,"%a %b %d %H:%M:%S +0000 %Y"))

### input: array array, typeless object
### output: typeless 
### example: findInArray(tweets, tweet)
def findInArray(array, object):
	for member in array:
		if member == object:
			return member
	return

### output: string
### example: getTweetsString()
def getTweetsString():
	tweets = None
	with open("p2000a.txt", "r") as f:
		tweets = f.read()
	with open("p2000b.txt", "r") as f:
		tweets = tweets + "\n" + f.read()
	return tweets
	
### output: array
### example: getTweetsArray()
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
### example: getTweetsByAttributes(tweets, ["user", "name"], "p2000rotterdam")
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
### example: getTweetsByAttributesWithFind(tweets, ["user", "name"], "amsterdam")
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
	
### input: array tweets, array objectKeys, array dictKeys, string val
### output: array 
### example: getTweetsByAttributesInArray(tweets, ["entities", "hashtags"], ["text"], "Zwolle")
def getTweetsByAttributesInArray(tweets, objectKeys, dictKeys, val):
	filtered = []
	for objectAttribute in tweets:
		original = objectAttribute
		found = True
		for key in objectKeys:
			try: 
				objectAttribute = objectAttribute[key]
			except (KeyError, IndexError):
				found = False
				break
		if found: 
			for member in objectAttribute:
				dictAttribute = member
				found = True
				for key in dictKeys:
					try: 
						dictAttribute = dictAttribute[key]
					except (KeyError, IndexError):
						found = False
						break
				if found and dictAttribute == val:
					filtered.append(original)
					break
	return filtered

### input: array tweets, array keys
### output: array 
### example: getUniqueValues(tweets, ["user", "name"])
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
	if values == set():
		values = []
	return values
	
### input: array tweets, array objectKeys, array dictKeys
### output: array 
### example: getUniqueValuesInArray(tweets, ["entities", "hashtags"], ["text"])
def getUniqueValuesInArray(tweets, objectKeys, dictKeys):
	values = []
	for objectAttribute in tweets:
		original = objectAttribute;
		found = True
		for key in objectKeys:
			try: 
				objectAttribute = objectAttribute[key]
			except (KeyError, IndexError):
				found = False
				break
		if found:
			for member in objectAttribute:
				dictAttribute = member
				found = True
				for key in dictKeys:
					try: 
						dictAttribute = dictAttribute[key]
					except (KeyError, IndexError):
						found = False
						break
				if found:
					values.append(dictAttribute)
	values = set(values)
	if values == set():
		values = []
	return values
	
### input: array tweets, double t1, double t2
### output: array 
### example: getTweetsInTimeFrame(tweets, getUnixFromDate("Sun Nov 20 12:37:45 +0000 2011"), getUnixFromDate("Sun Dec 04 01:39:30 +0000 2011"))
def getTweetsInTimeFrame(tweets, t1, t2):
	filtered = []
	for tweet in tweets:
		unix = getUnixFromDate(tweet["created_at"])
		if unix > t1 and unix < t2:
			filtered.append(tweet)
	return filtered