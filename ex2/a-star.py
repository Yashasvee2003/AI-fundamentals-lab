import heapq
import sys
MAX = sys.maxsize

adj_list = {"A":[("B",9),("C",6)],
    "B" :[("D",5)],
    "C": [("D",8),("F",5)],
    "D" : [("G",6),("E",7)],
    "F" : [("G",7)],
    "E" : [("H",4)],
    "G" : [("H",8)]
    }



# this is our prio queue
openlist = []

closedlist = []

parents = {"A":"A" ,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None}

# heuristic values using manhattan dist
h = {"A" : 4, "B" : 3, "C" : 3, "D" : 2, "E" : 1, "F" : 2, "G" : 1, "H" : 0}

# for storing dist values (g values)
# A is our source
dist = {"A":0, "B":MAX, "C":MAX, "D":MAX, "E":MAX, "F":MAX, "G":MAX, "H":MAX}


def main():
    heapq.heappush(openlist,(h["A"]+dist["A"],"A"))
    i = 0

    while openlist:
        _, current_node = heapq.heappop(openlist)
        closedlist.append(current_node)
        if current_node == "H":
            break
        
        # add neighbours of current node to openlist
        neighbors = adj_list[current_node]

        # for each neighbour we have to find g score to calc f score
        # then we push to openlist
        for neighbor in neighbors:
            neighbor_node, neighbor_cost = neighbor
            if neighbor_node in closedlist:
                continue

            # new g score
            if dist[neighbor_node] > dist[current_node] + neighbor_cost:
                dist[neighbor_node] = dist[current_node] + neighbor_cost
                parents[neighbor_node] = current_node
                heapq.heappush(openlist,(h[neighbor_node]+dist[neighbor_node],neighbor_node))

        print(f"iteration {i}")
        print("openlist",openlist)
        print("closedlist",closedlist)
        print("parents",parents)
        print("dist",dist)
        print()
        print("*********************")
        i+=1
    
    print_path(parents)


        

def print_path(parents):
    path = []
    current_node = "H"
    while current_node != "A":
        path.append(current_node)
        current_node = parents[current_node]
    path.append("A")
    path.reverse()
    print("**********************")
    print("path to reach dest from source is:")
    print(path)




if __name__ == "__main__":
    main()