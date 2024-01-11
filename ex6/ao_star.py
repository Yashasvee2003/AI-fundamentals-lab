# performing AO star search on an AND OR graph

#Graph representation
g = {"A":["B","C","D"],"B":["E","F"],"C":["G","H","I"],"D":["J"]}

#Heuristic values
heuristics = {"A":999,"B":4,"C":2,"D":3,"E":6,"F":8,"G":2,"H":0,"I":0,"J":0}

#AND Arcs
and_arcs = {"A":["C","D"],"C":["H","I"]}

#Terminal states
terminal_states = ["E","F","G","H","I","J"]



def traverse_graph(g,heuristics,and_arcs,terminal_states,state):
    if(state in terminal_states):
        return heuristics[state]
    req_states = g[state]
    min_cost = 999
    cost = 0
    if state in and_arcs:
        min_cost = 0
        states = [i for i in req_states if i not in and_arcs[state]]
        req_states = states
        for i in and_arcs[state]:
            min_cost += 1 + traverse_graph(g,heuristics,and_arcs,terminal_states,i)
    for i in req_states:
        cost = 1 + traverse_graph(g,heuristics,and_arcs,terminal_states,i)
        if(cost < min_cost):
            min_cost = cost
    heuristics[state] = min_cost
    return heuristics[state]
    
def print_optimal_path(g,heuristics,and_arcs,state,terminal_states):
    #path = path.append(state)
    #print(path)
    print(state,"-",end = " ")
    if(state not in terminal_states):
        req_states = g[state]
        cost = 0
        if state in and_arcs:
            states = [i for i in req_states if i not in and_arcs[state]]
            req_states = states
            for i in and_arcs[state]:
                cost += heuristics[i] + 1
            if(heuristics[state] == cost):
                for i in and_arcs[state]:
                    print_optimal_path(g,heuristics,and_arcs,i,terminal_states)
        for i in req_states:
            if(heuristics[state] == heuristics[i] + 1):
                print_optimal_path(g,heuristics,and_arcs,i,terminal_states)
        
    
print("Optimal path cost: ",traverse_graph(g,heuristics,and_arcs,terminal_states,"A"))
print("Updated heuristics")
for i in heuristics:
    print(i,":",heuristics[i])
print("Optimal path:")
print_optimal_path(g,heuristics,and_arcs,"A",terminal_states)
        
