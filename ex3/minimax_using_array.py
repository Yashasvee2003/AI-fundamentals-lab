def create_full_binary_tree(i, n):

    tree = []
    tree.append(i)
    val = 2*i + 1
    for i in range(1,n+1):
        
        row_val = val
        for j in range(2**i):
            tree.append(row_val)
            row_val += 1

        val = val*2 + 1

    return tree



def minimax(tree,n):
    if n%2 == 0:
        findMax = False
    else:
        findMax = True

    num = len(tree)
    j = 1
    while num//2**j != 0:
        for i in range(num//2**(j+1), num//2**j):
            # print(tree[i], end = " ")
            if findMax:
                tree[i] = max(tree[2*i+1], tree[2*i+2])
            else:
                tree[i] = min(tree[2*i+1], tree[2*i+2])
        findMax = not(findMax)
        print()
        j+= 1

def print_path(oldTree, newTree):
    maxEle = newTree[0]
    print("path from root to required utility value :", end= " ")
    for i in range(len(newTree)):
        if maxEle == newTree[i]:
            print(oldTree[i], end="->")
    


n = 2
i = 1

oldTree = create_full_binary_tree(i,n)
print(f"tree: {oldTree}")
newTree = oldTree.copy()
minimax(newTree, n)
print("tree after calling minimax : ", newTree)

print_path(oldTree, newTree)




    
        




