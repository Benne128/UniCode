"""A graph data structure that uses adjacency matrix to add new nodes to the tree and also print the adjacent nodes also """
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
#dictionary 2 (new element)
new_node_vertex_dict = {}
new_node_vertex_dict [10] = [9]


#test 
print("Adjacent neighbors of vertex 8: ", un_weighted_graph_dict[8])
print("Adjacent neighbors of vertex 3: ", un_weighted_graph_dict[3])
 
print("node with adjacent vertex")
#add dictionary 2 to dictionary 1
un_weighted_graph_dict.update(new_node_vertex_dict)
#returns elements in the list 
i = len(un_weighted_graph_dict)
for i in range(0,i):
    print(i,":", un_weighted_graph_dict[i])


