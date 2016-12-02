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

#depth first search
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

#Dijkstra's algorithm
def Dijkstra(un_weighted_graph_dict, start, destination):
  scanned == start
  for all nodes in un_weighted_graph_dict.vertices
    n.tw == .
  s.tw == 0 
  visited []
  while vertices destination 
    for all vertices, u ,adjacent to vars 
      if v.tw+v[u].w < u.tw
      u.tw <- v.tw+v[u].w
      u.preveious <-v
    visited.append(v)
    min == .
    for all nodes n E v
      if e/ visited ^ n.tw < min
        v == n
        min == n.tw
 
print("node with adjacent vertex")
#add dictionary 2 to dictionary 1
un_weighted_graph_dict.update(new_node_vertex_dict)
#returns elements in the list 
i = len(un_weighted_graph_dict)
for i in range(0,i):
    print(i,":", un_weighted_graph_dict[i])


# needs preveious, weight and  destination sourse = start node 
