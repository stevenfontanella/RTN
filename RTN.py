from random import random,randint,choice
from abc import ABC, abstractmethod

#TODO: Capitalize first word?, possibly using a different type of node or an additional parameter?

class RTN:
	def __init__(self,start=None,end=None):
		if start is None:
			self.start=SimpleNode()
		else:
			self.start=start

		if end is None:
			self.end=None
		else:
			self.end=end

	def connect(self,RTN):
		self.end.connect(RTN.start)

	def eval(self):
		return " ".join(self)

	def __iter__(self):

		#start at successor of start because start does not have any information
		current=self.start.next()
		#yield current.eval()
		while(current is not None):
			yieldVal=current.eval()
			#print(yieldVal)
			if(yieldVal != ""):
				yield yieldVal
			current=current.next()

class Node(ABC):

	def __init__(self,name="Node"):
		self.connections=[]
		self.start=self.end=self
		self.name=name

	@abstractmethod
	def eval(self):
		raise NotImplementedError

	#one sided connection; self -> SimpleNode
	def connect(self,RTN):
		self.end.connections.append(RTN.start)

	#choose a neighboring node randomly
	def next(self):
		try:
			return choice(self.connections)
		except IndexError:
			return None

	def __str__(self):
		return self.name

'''
A complex node is an RTN in itself, but doesn't know how it's defined until
it needs to be evaluated, preventing infinite recursion
'''
class ComplexNode(Node):
	def __init__(self,generatorfn,name="ComplexNode"):
		super().__init__(name)
		self.fn=generatorfn

	def eval(self):
		return self.fn().eval()


class SimpleNode(Node):
	#name is mostly for debugging, might change to dict later
	def __init__(self,words,name="SimpleNode"):
		super().__init__(name)
		self.words=words

	#pick a random element from self.words
	def eval(self):
		return choice(self.words)

'''
Ornate Noun generator
'''
def ornateNoun(nouns=None,adjectives=None,articles=None):
	if nouns is None:
		with open("words/nouns.txt") as nounsList:
			nouns=list(map(str.strip,nounsList))
	if adjectives is None:
		with open("words/adjectives.adj") as adjList:
			adjectives=list(map(str.strip,adjList))
	if articles is None:
		articles=["a","an","the"]

	begin=SimpleNode([""],"begin")
	end=SimpleNode([""],"end")
	noun=SimpleNode(nouns,"noun")
	adjective=SimpleNode(adjectives,"adjective")
	article=SimpleNode(articles,"article")

	#structure of an Ornate Noun from Douglas Hofstadter's book, "Godel, Escher, Bach"
	begin.connect(article)
	begin.connect(adjective)
	begin.connect(noun)

	article.connect(adjective)
	article.connect(noun)

	adjective.connect(adjective)
	adjective.connect(noun)

	noun.connect(end)

	rtn=RTN(begin,end)

	return rtn

'''
Fancy Noun from Douglas Hofstadter's "Godel, Escher, Bach"
'''
def FancyNoun(nouns=None,verbs=None,adjectives=None,articles=None,pronouns=None,prepositions=None):
	ornate=ornateNoun()
	if pronouns is None:
		pronouns=["that","which","whom","who","whoever","whomever","whichever"]
	if prepositions is None:
		with open("words/prepositions.txt") as prepList:
			prepositions=list(map(str.strip,prepList))
	if nouns is None:
		with open("words/nouns.txt") as nounsList:
			nouns=list(map(str.strip,nounsList))
	if adjectives is None:
		with open("words/adjectives.adj") as adjList:
			adjectives=list(map(str.strip,adjList))
	if articles is None:
		articles=["a","an","the"]
	if verbs is None:
		with open("words/verbs.txt") as verbList:
			verbs=list(map(str.strip,verbList))

	begin=SimpleNode([""])
	end=SimpleNode([""])

	relativePronoun=SimpleNode(pronouns,"relative pronoun")
	ornate=ornateNoun()
	preposition=SimpleNode(prepositions,"preposition")
	verb1=SimpleNode(verbs,"verb1")
	verb2=SimpleNode(verbs,"verb2")
	fancy1=ComplexNode(FancyNoun,"fancy1")
	fancy2=ComplexNode(FancyNoun,"fancy2")
	fancy3=ComplexNode(FancyNoun,"fancy3")

	#set the structure of the RTN
	begin.connect(ornate)

	ornate.connect(relativePronoun)
	ornate.connect(preposition)
	ornate.connect(end)

	relativePronoun.connect(verb1)
	relativePronoun.connect(fancy2)

	verb1.connect(fancy1)

	fancy2.connect(verb2)

	preposition.connect(fancy3)

	fancy1.connect(end)

	verb2.connect(end)

	fancy3.connect(end)

	rtn=RTN(begin)
	return rtn


def ornateTest():
	ornatenouns=ornateNoun()

	for i in range(100):
		print(ornatenouns.eval())

def SimpleRecur():
	with open("words/nouns.txt") as nounsList:
		nouns=list(map(str.strip,nounsList))

	begin=SimpleNode([""],"begin")
	end=SimpleNode([""],"end")
	noun=SimpleNode(nouns,"noun")
	compl=ComplexNode(SimpleRecur,"recur")

	begin.connect(noun)
	begin.connect(compl)

	noun.connect(end)

	compl.connect(end)

	return RTN(begin,end)

if __name__=="__main__":

	#ornateTest()

	s=FancyNoun()

	for i in range(10):
		print(s.eval())

	# for i in s:
	# 	print(s.eval())
