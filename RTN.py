from random import random

class RTN:
	def __init_(self):
		self.start=None
		self.finish=None
		self.connections=[]

	def connect(self,RTN):
		self.connections.append(RTN)

	def eval(self):
		return eval(self.start)



class Node(RTN):
	def __init__(self,words):
		self.connections=[]
		self.words=words
	def connect(self,RTN): #one sided connection; self -> node
		self.connections.append(RTN)
	def eval(self):
		words[random()*len(words)]


#maybe get rid of the subclasses and instead associate each node with a file instead
#also RTNs need to act as nodes
class Adjective(Node):
	def __init__(self):
		self.dict=open("")
	def eval(self):



def randLine(file):
	return file[random()*len(file)]


def ornateNoun():




if __name__=="__main__":
	with open("words/nouns.txt") as nouns:
		n=list(nouns)
		print(n[100])
