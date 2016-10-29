class Vertex():
	def __init__(self, vid, vlabel):
		self.id = vid
		self.dfs_id = 0
		self.edges = []
		self.label = vlabel


class Edge():
	def __init__(self, vfrom, vto, elabel):
		self.vfrom = vfrom
		self.vto = vto
		self.label = elabel

class Graph():
	def __init__(self, gid, code=[]):
		self.id = gid
		self.edges = []
		self.vertices = []
		if len(code) != 0:
			self.rebulid_from_DFSCode(code)

	def add_vertex(self, vertex):
		self.vertices.append(vertex)

	def add_edge(self, edge):
		self.edges.append(edge)

	def get_vertex(self, vid):
		for v in self.edges:
			if v.id == vid:
				return v
		raise KeyError('vertex id error')

	def toDFSCode(self):
		DFSCode = []
		for e in self.edges:
			DFSCode.append((e.vfrom.id, e.vto.id, e.vfrom.label, e.vto.label, e.label))
		return DFSCode

	def rebuild_from_DFSCode(code):
		vertices = []
		for vfrom_id, vto_id, vfrom_label, vto_label, e_label in code:
			for vid, vlabel in [(vfrom_id, vfrom_label), (vto_id, vto_label)]:
				if not (vid, vlabel) in vertices:
					vertices.append((vid, vlabel))
		for vid, vlabel in vertices:
			self.add_vertex(Vertex(id=vid, label=vlabel))

		for vfrom_id, vto_id, vfrom_label, vto_label, e_label in code:
			vfrom = self.get_vertex(vfrom_id)
			vto = self.get_vertex(vto_id)
			self.add_edge(Edge(vfrom=vfrom, vto=vto, vlabel=elabel))

class gSpan():
	def __init__(self):
		self.id = 0
		self.minsup = 0
		self.graphs = []
	
	def readfile(self, filename):
		inputfile = open(filename)
		for line in inputfile.readlines():
			tmp = line.split(' ')
			if len(tmp) < 2:
				continue
			if tmp[0] == 't':
				self.graphs.append(Graph(tmp[2]))
			elif tmp[0] == 'v':
				self.graphs[-1].add_vertex(Vertex(vid=tmp[1], vlabel=tmp[2]))
			elif tmp[0] == 'e':
				vform = self.graphs[-1].get_vertex(tmp[1])
				vto = self.graphs[-1].get_vertex(tmp[2])
				self.graphs[-1].add_edge(Edge(vfrom=vfrom, vto=vto, elabel=tmp[3]))

	def run(self, msup):
		self.minsup = msup
