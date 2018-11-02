import json, time

serviceSubstrings = {
	"police": ["Prio 1:", "Prio 2:", "Prio 3:", "Prio: 1 ", "Prio: 2 ", "Prio: 3 ", "Prio 1 ", "Prio 2 ", "Prio 3 "],
	"ambulance": ["A1 " , "A2 ", "B ", "B1 ", "B2 "],
	"fireBrigade": ["BR 1 ", "BR 2 ", "HV 1 ", "HV 2 " , "HV 3", "PRIO 1 ", "PRIO 2 ", "PRIO 3 "]
}
prioritySubstrings = {
	"1": ["A1", "P 1", "Prio: 1", "PRIO 1", "Prio 1:", "Prio 1 ", "HV 1 ", "BR 1 "],
	"2": ["A2", "P 2", "Prio: 2", "PRIO 2", "Prio 2:", "Prio 2 ", "HV 2 ", "BR 2 "],
	"3": ["B ", "B1 ", "B2 ", "P 3", "Prio: 3", "PRIO 3", "Prio 3:", "Prio 3 ", "HV 3 "]
}
abbreviations = {
	"adam": "Amsterdam",
	"rdam": "Rotterdam",
	"zwol": "Zwolle",
	"lwar": "Leeuwarden",
	"nhln": "NHN",
	"tilb": "Tilburg",
	"gtrb": "Geertruidenberg",
	"harw": "Harderwijk",
	"oldb": "Oldeburg",
	"oned": "MON",
	"police": "police",
	"ambu": "ambulance",
	"firebrig": "fireBrigade",
	"prio1": "1",
	"prio2": "2",
	"prio3": "3",
	"othr": "other"
}

regions = {"Amsterdam", "Rotterdam", "Zwolle", "Leeuwarden", "NHN", "Tilburg", "Geertruidenberg", "Harderwijk", "Oldeburg", "MON"}
services = {"ambulance", "police", "fireBrigade"}
priorities = {"1", "2", "3"}

debug = False

### input: string date
### output: double
### example: getUnixFromDate("Wed Sep 18 20:17:17 +0000 2013")
def getUnixFromDate(date):
	return time.mktime(time.strptime(date,"%a %b %d %H:%M:%S +0000 %Y"))

### input: string string
### output: double
### example: getUnixFromDateString("10-10-2018")
def getUnixFromDateString(string):
	return time.mktime(time.strptime(string, "%Y-%m-%d"))

### input: string string
### output: double
### example: getSecondsFromTime("22:00")
def getSecondsFromTime(string):
	hours = int(string[:2]) or 0
	minutes = int(string[3:]) or 0
	return hours*3600 + minutes*60
	
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
	with open("p2000.txt", "r") as f:
		tweets = f.read()
	return tweets
	
### output: array
### example: getTweetsArray()
def getTweetsArray():
	tweets = []
	with open("p2000.txt", "r") as f:
		lines = f.readlines()
		for line in lines:
			tweets.append(json.loads(line))
	return tweets

### input: array tweets, array keys
### output: array
### example: sortTweetsByAttributes(tweets, ["favorite_count"])
def sortTweetsByAttributes(tweets, keys, reverse=False):
	if len(tweets) <= 1:
		return tweets[:]
	else:
		mi = len(tweets) // 2
		fst = sortTweetsByAttributes(tweets[:mi], keys, reverse)
		snd = sortTweetsByAttributes(tweets[mi:], keys, reverse)
		res = []
		fi, si = 0, 0
		while fi < len(fst) and si < len(snd):
			first = fst[fi]
			second = snd[si]
			for key in keys:
				try: 
					first = first[key]
				except (KeyError, IndexError):
					first = 0
			for key in keys:
				try: 
					second = second[key]
				except (KeyError, IndexError):
					second = 0
			if not descend:
				if first <= second:
					res.append(fst[fi])
					fi += 1
				else:
					res.append(snd[si])
					si += 1
			else:
				if first >= second:
					res.append(fst[fi])
					fi += 1
				else:
					res.append(snd[si])
					si += 1
		if fi < len(fst):
			res.extend(fst[fi:])
		elif si < len(snd):
			res.extend(snd[si:])
		return res
		
### input: array tweets, array keys, string val
### output: array 
### example: getTweetsByAttributes(tweets, ["user", "name"], "p2000rotterdam")
def getTweetsByAttributes(tweets, keys, val):
	filtered = []
	for tweet in tweets:
		if hasTweetAttributes(tweet, keys, val):
			filtered.append(tweet)
	return filtered

### input: array tweets, array keys, string substring
### output: array 
### example: getTweetsByAttributesWithFind(tweets, ["user", "name"], "amsterdam")
def getTweetsByAttributesWithFind(tweets, keys, substring):
	filtered = []
	for tweet in tweets:
		if hasTweetAttributesWithFind(tweet, keys, substring):
			filtered.append(tweet)
	return filtered
	
### input: array tweets, array objectKeys, array dictKeys, string val
### output: array 
### example: getTweetsByAttributesInArray(tweets, ["entities", "hashtags"], ["text"], "Zwolle")
def getTweetsByAttributesInArray(tweets, objectKeys, dictKeys, val):
	filtered = []
	for tweet in tweets:
		if hasTweetsAttributesInArray(tweet, objectKeys, dictKeys, val):
			filtered.append(tweet)
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
	values = list(values)
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
	values = list(values)
	return values
	
### input: array tweets, double t1, double t2
### output: array 
### example: getTweetsInTimeFrame(tweets, getUnixFromDate("Sun Nov 20 12:37:45 +0000 2011"), getUnixFromDate("Sun Dec 04 01:39:30 +0000 2011"))
def getTweetsInTimeFrame(tweets, t1, t2):
	filtered = []
	for tweet in tweets:
		if isTweetInTimeFrame(tweet, t1, t2):
			filtered.append(tweet)
	return filtered
	
### input: array tweets, int num
### output: array 
### example: getTweetsWithPriority(tweets, 1)
def getTweetsWithPriority(tweets, num):
	filtered = []
	for tweet in tweets:
		if isTweetPriority(tweet, num):
			filtered.append(tweet)
	return filtered

### input: array tweets, string service
### output: array 
### example: getTweetsWithService(tweets, "fireBrigade")
def getTweetsWithService(tweets, service):
	filtered = []
	for tweet in tweets:
		if isTweetService(tweet, service):
			filtered.append(tweet)
	return filtered

### input: object attribute, array keys, string val
### output: bool 
### example: hasTweetAttributes(tweet, ["user", "name"], "p2000rotterdam")
def hasTweetAttributes(attribute, keys, val):
	found = True
	for key in keys:
		try: 
			attribute = attribute[key]
		except (KeyError, IndexError):
			found = False
			break
	return found and attribute == val

### input: object attribute, array keys, string substring
### output: bool
### example: hasTweetAttributesWithFind(tweet, ["user", "name"], "amsterdam")
def hasTweetAttributesWithFind(attribute, keys, substring, lower=True):
	found = True
	for key in keys:
		try: 
			attribute = attribute[key]
		except (KeyError, IndexError):
			found = False
			break
	if not lower:
		return found and not attribute.find(substring) == -1
	else:
		return found and not attribute.lower().find(substring.lower()) == -1
	
### input: object objectAttribute, array objectKeys, array dictKeys, string val
### output: bool
### example: hasTweetAttributesInArray(tweet, ["entities", "hashtags"], ["text"], "Zwolle")
def hasTweetAttributesInArray(objectAttribute, objectKeys, dictKeys, val):
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
				return True
	return False

### input: object tweet, int priority
### output: bool
### example: isTweetPriority(tweet, 1)
def isTweetPriority(tweet, priority):
	substrings = None
	try:
		substrings = prioritySubstrings[priority]
	except AttributeError:
		return False
	for substring in substrings:
		if hasTweetAttributesWithFind(tweet, ["text"], substring, False):
			return True
	return False
	
### input: object tweet, string service
### output: bool
### example: isTweetService(tweet, "fireBrigade")
def isTweetService(tweet, service):
	substrings = None
	try:
		substrings = serviceSubstrings[service]
	except AttributeError:
		return False
	for substring in substrings:
		if hasTweetAttributesWithFind(tweet, ["text"], substring, False):
			return True
	return False
			
### input: object tweet, double t1, double t2
### output: bool
### example: isTweetInTimeFrame(tweet, 1379528870.0, 1379530847.0)
def isTweetInTimeFrame(tweet, t1, t2):
	unix = getUnixFromDate(tweet["created_at"])
	return unix > t1 and unix < t2
		
### input: array tweets
### example: printContents(tweets)
def printContents(tweets):
	for tweet in tweets:
		print(tweet["text"])

### input: dictionary filters
### output: dictionary
### example: convertFilters({'adam': ['on'], 'rdam': ['on'], 'zwol': ['on'], 'lwar': ['on'], 'nhln': ['on'], 'tilb': ['on'], 'gtrb': ['on'], 'harw': ['on'], 'oldb': ['on'], 'oned': ['on'], 'police': ['on'], 'ambu': ['on'], 'firebrig': ['on'], 'prio1': ['on'], 'prio2': ['on'], 'prio3': ['on'], 'time-start': '', 'time-end': '', 'date-start': '', 'date-end': ''})
def convertFilters(form):
	converted = {
		"cities": {
			"Amsterdam": False,
			"Rotterdam": False,
			"Zwolle": False,
			"Leeuwarden": False,
			"NHN": False,
			"Tilburg": False,
			"Geertruidenberg": False,
			"Harderwijk": False,
			"Oldeburg": False,
			"MON": False
		},
		"services": {
			"police": False,
			"ambulance": False,
			"fireBrigade": False
		},
		"priorities": {
			"1": False,
			"2": False,
			"3": False
		},
		"time": {
			"time-start": -1,
			"time-end": -1,
			"date-start": -1,
			"date-end": -1
		},
		"other": False
	}
	for index in form:
		if index == "adam" or index == "rdam" or index == "zwol" or index == "lwar" or index == "nhln" or index == "tilb" or index == "gtrb" or index == "harw" or index == "oldb" or index == "oned":
			if not form[index] == []:
				converted["cities"][abbreviations[index]] = True
		elif index == "police" or index == "ambu" or index == "firebrig":
			if not form[index] == []:
				converted["services"][abbreviations[index]] = True
		elif index == "prio1" or index == "prio2" or index == "prio3":
			if not form[index] == []:
				converted["priorities"][abbreviations[index]] = True
		elif index == "date-start" or index == "date-end":
			if not form[index] == "":
				converted["time"][index] = getUnixFromDateString(form[index])
		elif index == "time-start" or index == "time-end":
			if not form[index] == "":
				converted["time"][index] = getSecondsFromTime(form[index])
		elif index == "othr":
			if not form[index] == []:
				converted[abbreviations[index]] = True
	return converted

### input: object tweet, dictionary filters
### output: bool
### example: filterTweet(tweet, {'adam': ['on'], 'rdam': ['on'], 'zwol': ['on'], 'lwar': ['on'], 'nhln': ['on'], 'tilb': ['on'], 'gtrb': ['on'], 'harw': ['on'], 'oldb': ['on'], 'oned': ['on'], 'police': ['on'], 'ambu': ['on'], 'firebrig': ['on'], 'othr': ['on'], 'prio1': ['on'], 'prio2': ['on'], 'prio3': ['on'], 'time-start': '', 'time-end': '', 'date-start': '', 'date-end': ''})
def filterTweet(tweet, filters):
	filters = convertFilters(filters)
	citiesFilter = False
	servicesFilter = False
	prioritiesFilter = False
	timeFilter = False
	otherFilter = False
	otherCities = True
	otherServices = True
	otherPriorities = True
	for filter in filters:
		if filter == "cities":
			for attribute in filters[filter]:
				if filters[filter][attribute]:
					if (hasTweetAttributesWithFind(tweet, ["user", "name"], attribute) or hasTweetAttributesWithFind(tweet, ["text"], attribute)):
						citiesFilter = True
						break
		elif filter == "services":
			for attribute in filters[filter]:
				if filters[filter][attribute]:
					if isTweetService(tweet, attribute):
						servicesFilter = True
						break
		elif filter == "priorities":
			for attribute in filters[filter]:
				if filters[filter][attribute]:
					if isTweetPriority(tweet, attribute):
						prioritiesFilter = True
						break
		elif filter == "time":
			filter = filters[filter]
			t1 = 0
			t2 = time.time()
			startd = filter["date-start"]
			endd = filter["date-end"]
			if not startd == -1:
				t1 = startd
			if not endd == -1:
				t2 = endd
			if isTweetInTimeFrame(tweet, t1, t2):
				startt = filter["time-start"] 
				endt = filter["time-end"]
				remainder = (getUnixFromDate(tweet["created_at"]) + 7200)%86400 # timezone perhaps?
				if debug:
					print("startt " + str(startt) + ", endt: " + str(endt) + ", remainder: " + str(remainder))
				if not startt == -1 and not endt == -1:
					if endt > startt:
						timeFilter = remainder >= startt and remainder <= endt
					else:
						timeFilter = remainder >= endt and remainder <= startt
				elif not startt == -1:
					timeFilter = remainder >= startt
				elif not endt == -1:
					timeFilter = remainder <= endt
				else:
					timeFilter = True
		elif filter == "other":
			if filters[filter]:
				otherFilter = True
				for region in regions:
					if hasTweetAttributesWithFind(tweet, ["user", "name"], region) or hasTweetAttributesWithFind(tweet, ["text"], region):
						otherCities = False
						break
				for service in services:
					if isTweetService(tweet, service):
						otherServices = False
						break
				for priority in priorities:
					if isTweetPriority(tweet, priority):
						otherPriorities = False
						break
	if debug:
		print("oC: " + str(otherCities) + ", oP: " + str(otherPriorities) + ", oS: " + str(otherServices) + ", oF: " + str(otherFilter) + ", cF: " + str(citiesFilter) + ", pF: " + str(prioritiesFilter) + ", sF: " + str(servicesFilter) + ", tF: " + str(timeFilter))
	compliesWithMainFilters = citiesFilter and prioritiesFilter and servicesFilter
	return compliesWithMainFilters and timeFilter or otherFilter and timeFilter and (otherCities or otherServices or otherPriorities)