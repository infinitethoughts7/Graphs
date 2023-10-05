adj_List =  {
    
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["B", "F"], 
    "D" : [],
    "E" : ["F"],
    "F" : []
}
#print(adj_List["A"])

clr = {}
prt = {}
trv_t  = {}
dfs_trav_path = []

for i in adj_List.keys():
    clr[i] = "R"
    prt[i] = None
    trv_t[i] = [-1, -1]
#print(clr)
# DFS Algo
time = 0

def depth_free_search(node):
    global time 
    clr[node] = "B"
    trv_t[node][0] = time 
    dfs_trav_path.append(node)
    time += 1
    for neighbour in adj_List[node]:
        if clr[neighbour] == "R":
            prt[neighbour] = node
            depth_free_search(neighbour)
    clr[node] = "G"
    trv_t[node][1] = time 
    time +=1
depth_free_search("A")
print(f"Dfs_trav_path:\n :{dfs_trav_path}")
print()
print(f"Updated colours:\n: {clr}")
print()
print(f"Traversal time to reach node:\n {trv_t}")
print()
print(f"Parents of the nodes:\n{prt}")
print()
print("Traversal time:")
for node in trv_t.keys():

    print(f"{node, trv_t[node]}")
