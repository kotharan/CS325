#this will represent each node on the graph 
class node():
    def __init__(self, value, component):
        self.value = value;
        self.component = component;


#this will represent the connection between two two nodes
class edge():
	def __init__(self, v1, v2, weight):
		self.v1 = v1;
		self.v2 = v2;
		self.weight = weight;

# this will comntain a list of all nodes and a list of all Edges
class Graph():
	def __init__(self, Vertices, Edges):	
		self.Verteces = Vertices;
		self.Edges = Edges;

#this will contain a list of all nodes and a list of the edges that are in the MST
class MST():
	def __init__(self, Vertices, Edges, weight):
		self.Vertices = Vertices;
		self.Edges = Edges;
		self.weight = weight;


def Boruvkas(Vertices, Edges):
	
	num_verts = len(Vertices);
	num_edges = len(Edges);
	num_comps = len(Verticies);
	mst_weight = 0;

	s = [None for i in range(num_comps)];	#keeps track of the safe edge for each connected component
	labels = [0 for i in range(n)];  #keeps track of which connected component each vertex is in
	for i in range(n):
		labales[i] = i;

	while(num_comps > 1):

		for i in range(num_comps):	#initialize the safe edge for each component to be null
			s[i] = None;


		#count and label
		for i in range(num_edges):

			if(labels[Edges[i].v1.value] != labels[Edges[i].v2.value]): #if the endpoints are part of different components
				#check if its the cheapest edge you have seen so far for either of the two components
				if(s[labels[Edges[i].v1.value]] == None || s[labels[Edges[i].v1.value]].weight > Edges[i].weight):
					s[labels[Edges[i].v1.value]] = Edges[i];

				if(s[labels[Edges[i].v2.value]] == None || s[labels[Edges[i].v2.value]].weight > Edges[i].weight):
					s[labels[Edges[i].v2.value]] = Edges[i];

		for i in range(num_comps): #now readjust labels to reflect the new edges that hace been added in s[]. You never use vertex.component so no need to update it. 

			new_edge = s[i];
			mst_weight = mst_weight + new_edge.weight;

			if (labels[new_edge.v1.value] != labels[new_edge.v2.value]):
				old_comp = labels[new_edge.v2.value];
				for i in range(num_vertices):
					if(labels[i] == old_comp):
						labels[i] = labels[new_edge.v1.value];
				num_comps = num_comps - 1;



# def min_span_tree(Data, g):

# 	mst = MST(g.Vertices, [None for i in range(len(g.Edges))], 0);
# 	mst_len = 0;
# 	n = len(g.Vertices);
# 	num_comps = n;	#the number of components in the graph

# 	s = [None for i in range(num_comps)];	#keeps track of the safe edge for each connected component

# 	labels = [0 for i in range(n)];  #keeps track of which connected component each vertex is in
# 	for i in range(n):
# 		labales[i] = i;

# 	while(num_comps > 1):	#When there is one component the graph is an mst

# 		for i in range(num_comps):	#initialize the safe edge for each component to be null
# 			s[i] = None;

# 		for i in range(len(g.Edges)):	# walk through the list of edges

# 			if(g.Edges[i].v1.component != g.Edges[i].v2.component):		#if the endpoints are part of different components

# 				#check if its the cheapest edge you have seen so far for either of the two components
# 				if (s[g.Edges[i].v1.component] == None || s[g.Edges[i].v1.component] > g.Edges[i].weight):
# 						s[Edges[i].v1.component] = Edges[i];


# 				if (s[g.Edges[i].v2.component] == None || s[g.Edges[i].v2.component] > g.Edges[i].weight):
# 						s[g.Edges[i].v2.component] = g.Edges[i];

# 		for i in range(num_comps):	#walk through the safe edges, reset the number of components
# 			if (s[i] != None):
	
# 				if (s[i].v1.component != s[i].v2.component):	#if their components have not already been combined
# 					mst.Edges[mst_len] = s[i];	# add the edge to the mst
# 					mst_len++;
# 					num_comps = num_comps - 1;
# 					for j in range(n):
# 						if(labels[j] == s[i].v2.component):		
# 							labels[j] = s[i].v1.component;		#relabel the edge in the labels array

# 							Edges[j]
# 					s[i].v2.component = s[i].v1.component;




def build_data():
	#Data = [[0 for i in range(n)] for i in range(n)]; #graph's adj. matrix will replace with file itself
 
	#initialize the set of Verticies
	Vertices = [0 for i in range(n)];
	for i in range(n):
		newNode = node(i, i);
		Vertices[i] =  newNode;

	#initialize the set of Edges
	Edges = [0 for i in range((n*n))];
	k = 0;
	for i in range(n): # walk through the rows of the 2d array
		j = i+1;	#start at the unique element (since [0][1] is the same as [1][0], and [3][3] is not valuable information)
		while(j < n):
			newEdge = edge(Vertices[i], Vertices[j], Data[i][j]);
			Edges[k] = newEdge;
			k = k + 1;
			j = j + 1;

	#g = Graph(Vertices, Edges);



def main():
	#n = 5;	# n is the number of vertices, and th number of rows and cols in the adj matrix
			# in Boruvkas algorith it is also the number of connected components at the start.
			# at the start,
	build_data();
	return 0;

main();