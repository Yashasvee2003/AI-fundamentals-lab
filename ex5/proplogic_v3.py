import copy
'''
'(' LEFT BRACKET  SYMBOL ')' RIGHT BRACKET SYMBOL of highest precency=4,
'!': NOT SYMBOL with precedency=3,
'^': AND SYMBOL WITH PRECEDENCY=2,
'v': OR SYMBOL WITH PRECENDENCY=1,
'#': IMPLICATION SYMBOL and '$': BICONDITIONAL SYMBOL WITH PRECEDENCY=0
'''

msg='''\n 
\n'('  LEFT BRACKET SYMBOL              WITH PRECEDENCY=4 
\n')'  RIGHT BRACKET SYMBOL             WITH PRECEDENCY=4,
\n'!': NOT SYMBOL                       WITH PRECEDENCY=3,
\n'^': AND SYMBOL 		      WITH PRECEDENCY=2,
\n'v': OR SYMBOL  		      WITH PRECENDENCY=1,
\n'#': IMPLICATION SYMBOL 	      WITH PRECEDENCY=0
\n'$': BICONDITIONAL SYMBOL	      WITH PRECEDENCY=0\n\n'''

print(msg)

operators={'(':4,')':4,'!':3,'^':2,'v':1,'#':0,'$':0}
oplist="()!^v#$"

def andlogic(val1,val2):
	val1=int(val1)
	val2=int(val2)
	if [val1,val2]==[0,0]:
		return 0
	elif [val1,val2]==[0,1]:
		return 0
	elif [val1,val2]==[1,0]:
		return 0
	elif [val1,val2]==[1,1]:
		return 1
	
def orlogic(val1,val2):
	val1=int(val1)
	val2=int(val2)
	if [val1,val2]==[0,0]:
		return 0		
	elif [val1,val2]==[0,1]:
		return 1	
	elif [val1,val2]==[1,0]:
		return 1
	elif [val1,val2]==[1,1]:
		return 1

def notlogic(val1):
	val1=int(val1)
	if val1==0:
		return 1
	else:
		return 0

def implicationlogic(val1,val2):
	val1=int(val1)
	val2=int(val2)
	if [val1,val2]==[0,0]:
		return 1		
	elif [val1,val2]==[0,1]:
		return 1
	elif [val1,val2]==[1,0]:
		return 0
	elif [val1,val2]==[1,1]:
		return 1


def biconditionallogic(val1,val2):
	val1=int(val1)
	val2=int(val2)
	if [val1,val2]==[0,0]:
		return 1
	elif [val1,val2]==[0,1]:
		return 0
	elif [val1,val2]==[1,0]:
		return 0		
	elif [val1,val2]==[1,1]:
		return 1
recursion_counter=0

def evaluate(x):
	global recursion_counter
	
	#print("--"*recursion_counter)
	print("  "*recursion_counter,"Expression is:",x)
	global oplist
	global operators
	print()
	#print("  "*recursion_counter,"Before evaluating bracket EXPRESSION=",x)
	while('(' in x):
		ind0=x.index('(')
		x1="" 
		left_bracket_count=1
		right_bracket_count=0

		for i in range(ind0+1,len(x)):
			if x[i]==')':
				right_bracket_count+=1
				if left_bracket_count==right_bracket_count:
					break
				else:
					x1+=x[i]
			else:
				x1+=x[i]
				if x[i]=='(':
					left_bracket_count+=1

		x2=""
		x2+=x[:ind0]
	#	print()
	#	print("  "*recursion_counter,"Recursive call to execute=: ",x1)
		recursion_counter+=1
		x2+=evaluate(x1)  #recursive call to execute expressions within brackets
		ind2=ind0+len(x1)+2  #index to resume from
		x2+=x[ind2:]
		x=x2
	#print("  "*recursion_counter,"After evaluating bracket EXPRESSION=: ",x)	


	#if we are here, the expression passed to this function is completely with no brackets
	#print("\n")
	#print("  "*recursion_counter,"Before evaluating ! in  EXPRESSION=: ",x)	

	while('!' in x):
		x1=""
		ind=x.index('!')
		x1+=x[:ind]
		x1+=str(notlogic(x[ind+1]))
		x1+=x[ind+2:]
		x=x1

	#print("  "*recursion_counter,"After evaluating ! in  EXPRESSION=: ",x)	

	#print("\n")
	
	#print("  "*recursion_counter,"Before evaluating ^ in  EXPRESSION=: ",x)
	while('^' in x): 
		ind1=x.index('^')
		ind0=ind1-1  #left operand
		ind2=ind1+1  #right operand
		x1=""
		x1+=x[:ind0]
		
		x1+=str(andlogic(x[ind0],x[ind2]))
		x=x1
	
	#print("  "*recursion_counter,"After evaluating ^ in  EXPRESSION=: ",x)
	#print("\n")

	
	#print("  "*recursion_counter,"efore evaluating v in  EXPRESSION=: ",x)
	while('v' in x):
		ind1=x.index('v')
		ind0=ind1-1  #left operand
		ind2=ind1+1  #right operand
		x1=""
		x1+=x[:ind0]
		x1+=str(orlogic(x[ind0],x[ind2]))
		x1+=x[ind2+1:]
		x=x1
	
	#print("  "*recursion_counter,"After evaluating v in  EXPRESSION=: ",x)	
	
	
	#print("\n")
	
	#print("  "*recursion_counter,"Before evaluating # in  EXPRESSION=: ",x)
	while('#' in x):
		#print("inside # function",x)
		ind1=x.index('#')
		ind0=ind1-1  #left operand
		ind2=ind1+1  #right operand
		x1=""
		x1+=x[:ind0]
		x1+=str(implicationlogic(x[ind0],x[ind2]))
		x1+=x[ind2+1:]
		x=x1
	#print("  "*recursion_counter,"After evaluating # in  EXPRESSION=: ",x)
	
	#print("  "*recursion_counter,"Before evaluating $ in  EXPRESSION=: ",x)
	print()
	print()
	while('$' in x):
		ind1=x.index('$')
		ind0=ind1-1  #left operand
		ind2=ind1+1  #right operand
		x1=""
		x1+=x[:ind0]
		x1+=str(biconditionallogic(x[ind0],x[ind2]))
		x1+=x[ind2+1:]
		x=x1
	#print("  "*recursion_counter,"After evaluating $ in  EXPRESSION=: ",x)
	
	print("  "*recursion_counter,"returning ",x,"\n")
	recursion_counter-=1
	return x
	

exp=input("Enter expression with operators as mentioned above and operands as p and q only:")

def calculate(exp):
	global recursion_counter
	tt=[]
	exp1=copy.deepcopy(exp)
	exp2=copy.deepcopy(exp)
	exp3=copy.deepcopy(exp)
	exp4=copy.deepcopy(exp)

	exp1=exp1.replace('p','0')
	exp1=exp1.replace('q','0')

	exp2=exp2.replace('p','0')
	exp2=exp2.replace('q','1')

	exp3=exp3.replace('p','1')
	exp3=exp3.replace('q','0')

	exp4=exp4.replace('p','1')
	exp4=exp4.replace('q','1')


	print("EVALUATION BY SUBSTITUTING P=0,Q=0")
	recursion_counter=0
	tt.append(evaluate(exp1))

	print("-----------------------------")
	print("EVALUATION BY SUBSTITUTING P=0,Q=1")
	recursion_counter=0
	tt.append(evaluate(exp2))


	print("-----------------------------")
	print("EVALUATION BY SUBSTITUTING P=1,Q=0")
	recursion_counter=0
	tt.append(evaluate(exp3))

	print("-----------------------------")
	print("EVALUATION BY SUBSTITUTING P=1,Q=1")
	recursion_counter=0
	tt.append(evaluate(exp4))
	return tt

tt1=calculate(exp)

print("Truth Table")
print(tt1)
if(tt1==['1','1','1','1']):
	print("Tautological Expression")
else:
	print("Not a tautology")

a=input("\n\nEnter Expression-1 for the second question: ")
b=input("\n\nEnter Expression-2 for the second question: ")
print("\n\n--------------------------------------------------------------")
print("Calculating First Expression\n")
a_res=calculate(a)
print("\n\n--------------------------------------------------------------")
print("Calculating Second Expression\n")

b_res=calculate(b)
if(a_res==b_res):
	print(a," and expression ",b,"They are equal expressions")
	print("Truth table of exp-1 is: ",a_res)
	print("Truth table of exp-2 is: ",b_res)
	
	print(a," and expression ",b,"They are equal expressions")
else:
	print(a,"and ",b," are not equal")
	print("Truth table of exp-1 is: ",a_res)
	print("Truth table of exp-2 is: ",b_res)
	print(a," and expression ",b,"They are not equal expressions")