from random import random,randint

class RTN:
	def __init__(self,start=None,end=None):
		if start is None:
			self.start=Node()
		else:
			self.start=start

		if end is None:
			self.end=None
		else:
			self.end=end

	def connect(self,RTN):
		self.end.connect(RTN.start)

	def eval(self):
		string=""

		#start at the successor of start because start does not have any information
		current=self.start.next()
		while(current is not None):
			string+=current.eval()+" "
			current=current.next()

		return string

class Node:
	#name is mostly for debugging, might change to dict later
	def __init__(self,words=None,name="Node"):
		self.connections=[]
		self.words=words
		self.name=name
		self.start=self
		self.end=self
	def connect(self,RTN): #one sided connection; self -> node
		self.end.connections.append(RTN.start)

	#choose a neighboring node randomly
	def next(self):
		try:
			return self.connections[int(random()*len(self.connections))]
		except IndexError:
			return None
	def eval(self):
		#print(self.words[int(random())*len(self.words)])
		return self.words[int(random()*len(self.words))]

	def __str__(self):
		return self.name

#ornate noun generator
def ornateNoun(nouns=None,adjectives=None,articles=None):
	if nouns is None:
		with open("words/nouns.txt") as nounsList:
			nouns=list(map(str.strip,nounsList))
	if adjectives is None:
		with open("words/adjectives.adj") as adjList:
			adjectives=list(map(str.strip,adjList))
	if articles is None:
		articles=["a","an","the"]

	begin=Node([""],"begin")
	end=Node([""],"end")
	noun=Node(nouns,"noun")
	adjective=Node(adjectives,"adjective")
	article=Node(articles,"article")
	#structure of an Ornate Noun from Douglas Hofstadter's book, "Godel, Escher, Bach"
	begin.connect(article)
	begin.connect(adjective)
	begin.connect(noun)

	article.connect(adjective)
	article.connect(noun)

	adjective.connect(adjective)
	adjective.connect(noun)

	noun.connect(end)

	rtn=RTN(begin)

	return rtn

#May need to implement some sort of 'lazy evaluation' where the recursion is only evaluated when
#the recurring node is reached, otherwise it seems an infinite loop would occur
def FancyNouns(nouns=None,adjectives=None,articles=None,pronouns=None,prepositions=None):
	ornate=ornateNoun()
	if pronouns is None:
		pronouns=["that","which","whom","who","whoever","whomever","whichever"]
	if prepositions is None:
		with open("words/prepositions.txt") as prepList:
			prepositions=list(map(str.strip,prepList))
	if nouns is None:
		with open("words/nouns.txt") as nounsList:
			noun=Node(list(map(str.strip,nounsList)),"noun")
	if adjectives is None:
		with open("words/adjectives.adj") as adjList:
			adjective=Node(list(map(str.strip,adjList)),"adj")
	if articles is None:
		article=Node(["a","an","the"],"article")

	relativePronouns=Node(pronouns,"relative pronouns")

if __name__=="__main__":

	ornatenouns=ornateNoun()

	for i in range(100):
		print(ornatenouns.eval())
