"""here is a graph, using an adjacency matrix with implemented bfs and dfs which is then printed to a text file"""
#dictionary 1
un_weighted_graph_dict = {}


un_weighted_graph_dict[0] = [1,2]
un_weighted_graph_dict[1] = [0,2]
un_weighted_graph_dict[2] = [3,4]
un_weighted_graph_dict[3] = [2,4]
un_weighted_graph_dict[4] = [5]
un_weighted_graph_dict[5] = [6,7]
un_weighted_graph_dict[6] = [5,8]
un_weighted_graph_dict[7] = [8]
un_weighted_graph_dict[8] = [7,9]
un_weighted_graph_dict[9] = []
#dictionary 2 (add new element)
new_node_vertex_dict = {}
new_node_vertex_dict [10] = [9]


#test 
print("Adjacent neighbors of vertex 8: ", un_weighted_graph_dict[8])
print("Adjacent neighbors of vertex 3: ", un_weighted_graph_dict[3])

#dfs  
print("Depth first search")
def find_all_paths(un_weighted_graph_dict, start, end, path=[]):
  path.append([0])
  if start == end:
    return [path]
  else:
    path +1
  for node in un_weighted_graph_dict[0]:
    if node not in path:
      return None
print (un_weighted_graph_dict)

#adding new node to dict and printing 
print("node with adjacent vertex")
#add dictionary 2 to dictionary 1
un_weighted_graph_dict.update(new_node_vertex_dict)
#returns elements in the list 
i = len(un_weighted_graph_dict)
for i in range(0,i):
    print(i,":", un_weighted_graph_dict[i])
print ("Bredth first search")

def bfs(graph, start, path=[]):
    temp_path = [start]
	
    q.enqueue(temp_path)#creating a que for temp_path
	
    while q.IsEmpty() == False:
	      tmp_path = q.dequeue()#used for fast appends like push pop etc
	      last_node = tmp_path[len(tmp_path)-1]#last node = temporary path's lenght -1
	      print (tmp_path)
	      if last_node == end:# if the search reaches the correct or the end node it will print that its a valid path 
		      print ("VALID_PATH : "),tmp_path
	      for connecting_node in un_weighted_graph_dict [last_node]:
		      if connecting_node not in tmp_path:
			      new_path = []
			      new_path = tmp_path + [connecting_node]
			      q.enqueue(new_path)

print (bfs(un_weighted_graph_dict, start, path=[]))

with open("GraphTraversal.py") as text_file:#when file is opened print in text file
    print("Depth first search".format(find_all_paths), file=text_file)
  
