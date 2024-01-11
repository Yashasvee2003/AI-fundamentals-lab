def main():

	family = {(0,0):(-1,-1)}

	state_list = [(0,0)]
	for state in state_list:
		#print("The parent is ", state)	
		threeG,fourG = state	
		if threeG > 0:
			new_state = (0,fourG)
			if new_state not in state_list:
				family[new_state] = state
				#print("Child = ", new_state)
				state_list.append(new_state)
			
		if threeG < 3:
			new_state = (3,fourG)
			if new_state not in state_list:
				family[new_state] = state
				#print("Child = ", new_state)
				state_list.append(new_state)
			
		if fourG > 0:
			new_state = (threeG,0)
			if new_state not in state_list:
				family[new_state] = state
				#print("Child = ", new_state)
				state_list.append(new_state)
			
		if fourG < 4:
			new_state = (threeG,4)
			if new_state not in state_list:
				family[new_state] = state
				#print("Child = ", new_state)
				state_list.append(new_state)
		
		#4----> 3 Gallon		
		if threeG < 3 and fourG > 0:
			fillable = 3 - threeG
			# emptying 4G into 3G fully
			if fillable > fourG :
				
				new_state = (threeG+fourG, 0)
				
			else:
				new_state = (3 , fourG - fillable)
			if new_state not in state_list:
				family[new_state] = state
				#print("Child = ", new_state)
				state_list.append(new_state)
		
		#3 ---> 4 Gallon
		if threeG > 0 and fourG < 4:
			fillable = 4- fourG
			# emptying 3G into 4G fully
			if fillable > threeG:
				new_state = (0,threeG+fourG)
			else:
				new_state = (threeG - fillable,4)
			if new_state not in state_list:
				family[new_state] = state
				#print("Child = ", new_state)
				state_list.append(new_state)
		if new_state[1] == 2:
			printPath(family,new_state)
		#print(state)
			
		
		
					
	
def printPath(family,init_state):
	while(init_state != (-1,-1)):
		print(init_state,"----->",end ="")
		init_state = family[init_state]
	print()
		
			

main()