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

	def eval(self):
		string=""

		#start at the successor of start because start does not have any information
		current=self.start.next()
		while(current is not None):
			string+=current.eval()+" "
			current=current.next()

		return string

class Node:
	#name is mostly for debugging
	def __init__(self,words=None,name="Node"):
		self.connections=[]
		self.words=words
		self.name=name
	def connect(self,RTN): #one sided connection; self -> node
		self.connections.append(RTN)

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
def OrnateNoun(nouns=None,adjectives=None,articles=None):
	if nouns is None:
		with open("words/nouns.txt") as nounsList:
			noun=Node(list(map(str.strip,nounsList)),"noun")
	if adjectives is None:
		with open("words/adjectives.adj") as adjList:
			adjective=Node(list(map(str.strip,adjList)),"adj")
	if articles is None:
		article=Node(["a","an","the"],"article")

	begin=Node([""],"begin")
	end=Node([""],"end")
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

	while(True):
		yield rtn.eval()

if __name__=="__main__":

	ornatenouns=OrnateNoun()

	for i in range(100):
		print(next(ornatenouns))
