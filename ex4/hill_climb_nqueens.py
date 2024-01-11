# solving n queens problem using hill climb algorithm

#Importing Necessary Modules
import copy
import random

# Main Function 
def main():
    size = 4
    board = createBoard(size)
    print("Empty Board : \n")
    printBoard(board)
    print("Initial State:\n")
    generateStates(board)
    printBoard(board)
    #objective(board)
    hillclimb(board)


#Function to Create Inital Board
def createBoard(size):
    board = [["-" for _ in range(size)] for __ in range(size)]
    return board

#Function to Print Board
def printBoard(board):
    print()
    for row in board:
        print(row)
    print()

#Function To generate Inital Random State
def generateStates(board,count=0):
    if count == len(board):
        return    
    col = random.randint(0,len(board)-1)
    if board[count][col] == 'Q':
        generateStates(board,count)
    board[count][col] = 'Q'
    generateStates(board,count+1)

#Function to Calculate the number of attacking pairs
def objective(board):
    attacking_pairs = 0
    queen_pos = []
    for count in range(len(board)):
        queen_pos.append((count,board[count].index('Q')))
    #print(queen_pos)
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            #print(queen_pos[i],queen_pos[j])
            if(queen_pos[i][1] == queen_pos[j][1]):
                #print("Column: ",queen_pos[i],queen_pos[j])
                attacking_pairs +=1
            if( abs(queen_pos[i][0] - queen_pos[j][0]) == abs(queen_pos[i][1] - queen_pos[j][1])):
                attacking_pairs +=1
                #print("Diagonal : ",queen_pos[i],queen_pos[j])
    #print()
    #print(attacking_pairs)
    return attacking_pairs

#Function To Calculate Minimum State
def find_min(states):
    min_value = float('inf')
    min_state = None

    for child,value in states:
        if value < min_value:
            min_value = value
            min_state = child

    return min_state

#Hill Climb Function
def hillclimb(board,recursion_depth = 0):

    #Terminate when maximum recursion depth is reached or solution is found
    if recursion_depth == 3 or (objective(board)==0):
        return

    #Find position of queens
    states = []
    queen_pos = []
    for count in range(len(board)):
        queen_pos.append(board[count].index('Q'))
    
    #Generate all possible states and calculate the Objective Function Value
    for count in range(len(board)):        
        for col in range(len(board)):
            if col != queen_pos[count]:                
                child = copy.deepcopy(board)                
                child[count] = ["-" for _ in range(len(board))] 
                child[count][col] = "Q"
                #printBoard(child)
                #print("No. of Attacking Pairs = ",objective(child))
                #print("\n")
                states.append((child,objective(child)))

    #Print Minimum State and continue
    print(f"Min State for Iteration {recursion_depth+1} :\n")
    min_state = find_min(states)
    print("No. of Attacking Pairs = ",objective(min_state))
    printBoard(min_state)    
    hillclimb(min_state,recursion_depth+1)




main()
