# AB=9, AC=6, BD=5, CD=8, CF=5, DG=6, FG=7, DE=7,
# EH=4, GH=8
adj_list = {"A":[("B",9),("C",6)],
            "B" :[("D",5)],
            "C" : [("D",8), ("F",5)],
            "D" : [("G",6), ("E",7)],
            "F" : [("G",7)],
            "E" : [("H",4)],
            "G" : [("H",8)]
            }

DEST = (3,3)
visited = list()


coords = {"A":(1,1),"B":(1,2),"PIT":(0,0),
        "C":(2,1),"D":(2,2),"E":(2,3),
        "F":(3,1),"G":(3,2),"H":(3,3)}

def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    

def greedy_bfs(node, adj_list, coords):
    if node == "H":
        return
    neighbours = adj_list[node]
    minh,min_node = 9999, None
    for i in neighbours:
        coordinates_of_i = coords[i[0]]
        md = manhattan_dist(coordinates_of_i, DEST)
        if md < minh:
            minh = md
            min_node = i[0]
    # min neighbour found
    visited.append(min_node)
    print(f"node chosen :{min_node},manhattan dist of node :{minh}")
    greedy_bfs(min_node,adj_list,coords)                         


def main():
    # greedy bfs using manhattan dist
    visited.append("A")                                                                    
    greedy_bfs("A",adj_list,coords)
    print(visited)

                                                             



if __name__ == "__main__":
    main()







