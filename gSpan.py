class Edge():
	def __init__(self):
		self.id = 0
		self.vfrom = 0
		self.vto = 0
		self.label = 0

class Vertex():
	def __init__(self):
		self.edges = []
		self.label = 0	

class Graph():
	def __init__(self):
		self.edges = []



class DFS():
	def __init__(self):
		self.vfrom = 0
		self.vto = 0
		self.flabel = 0
		self.tlabel = 0

class DFSCode():
	def __init__(self):
		self.DFS = []
		self.rightMostPath = []

class PDFS():
	def __init__(self):
		self.id = 0
		self.edge = Edge()
		self.prev = None

class gSpan():
	def __init__(self):
		self.id = 0
		self.minsup = 0
		self.trans = []
		self.dfscode = None
		self.mindfscode = None
		self.mingraph = None
	