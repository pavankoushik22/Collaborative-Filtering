from math import sqrt

critics={'lisa rose':{'lady in the water':2.5,'snakes on a plane':3.5,'just my luck':3.0,'superman returns':3.5,'you,me and dupree':2.5,'the night listener':3.0},
'gene seymour':{'lad in the water':3.0,'snakes on a plane':3.5,'just my luck':1.5,'superman returns':5.0,'the night listener':3.0,'you,me and dupree':3.5},
'michael phillips':{'lady in the water':2.5,'snakes on a plane':3.0,'superman returns':3.5,'the night listener':4.0},
'claudia puig':{'snakes on a plane':3.5,'just my luck':3.0,'the night listener':4.5,'superman returns':4.0,'you,me and dupree':2.5},
'mick lasalle':{'lady in the water':3.0,'snakes on a plane':4.0,'just my luck':2.0,'superman returns':3.0,'the night listener':3.0,'you,me and dupree':2.0},
'jack matthews':{'lady in the water':3.0,'snakes on a plane':4.0,'the night listener':3.0,'superman returns':5.0,'you,me and dupree':3.5},
'toby':{'snakes on a plane':4.5,'you,me and dupree':1.0,'superman returns':4.0}}

def sim_distance(prefs,person1,person2):
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
	if(len(si)==0):return 0
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
	return(1/(1+sum_of_squares))

def sim_pearson(prefs,p1,p2):
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]:
			si[item]=1
	if(len(si)==0):return 0
	n=len(si)
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])
	
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if(den==0): return 0
	r=num/den
	return r

def topMatches(prefs,person,n=5,similarity=sim_pearson):
	scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
	scores.sort()
	scores.reverse()
	return(scores[0:n])

def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		if other==person:continue
		sim=similarity(prefs,person,other)
		if sim<=0:continue
		for item in prefs[other]:
			if(item not in prefs[person] or prefs[person][item]==0):
				totals.setdefault(item,0)
				totals[item]+=prefs[other][item]*sim
				simSums.setdefault(item,0)
				simSums[item]+=sim
	rankings=[(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
	return rankings
def transformPrefs(prefs):
	result={}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person]=prefs[person][item]
	return result

