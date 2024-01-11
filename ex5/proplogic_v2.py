# And is &, OR is |, NOT is ~, Implies is - and BI-Cond is =
def myand(p,q):
    res=[]
    for x in range(4):
        res.append(p[x]*q[x])
    return res


def myor(p,q):
    res=[]
    for x in range(4):
        if p[x]==1 and q[x]==1:
            res.append(1)
        else:
            res.append(p[x]+q[x])
    return res
    

def mynot(x):
    res=[]
    for i in x:
        if i==0:
            res.append(1)
        else:
            res.append(0)
    return res

def imply(p,q):
    res=[]
    for x in range(4):
        if p[x]==1 and q[x]==0:
            res.append(0)
        else:
            res.append(1)
    return res

def bicon(p,q):
    res=[]
    for x in range(4):
        if p[x] == q[x]:
            res.append(1)
        else:
            res.append(0)
    return res

def eval(operands,operators):
    print("Recieved = ", operands, operators)
    for i in range(len(operators)):
        if operators[i] =='~':
            #print("Found the NEGATE\n")
            operands[i] = mynot(operands[i])
            operands.insert(0,0)
            #operators.pop(i)       # Having an operator without moving forward in list of operands upsets the balance
            #i-=1                   # Removing the operator from the list and moving back one index to balance it
        elif operators[i] =='&':      #[q,p] [v]                        #[a,ba,c,d,eabcc] [^,^,^,^]   
            operands[i+1] = myand(operands[i],operands[i+1]) 
            #operators.pop(i)
        elif operators[i] == '|':
            operands[i+1] = myor(operands[i],operands[i+1])
        elif operators[i] == '-':
            operands[i+1] = imply(operands[i],operands[i+1])
        elif operators[i] == '=':
            operands[i+1] = bicon(operands[i],operands[i+1])
    return operands[-1]
    
            
    
#def is_tautology(e):
def is_tautology(ans):
    if ans==[1,1,1,1]:
        print("The given expression is a tautology\n")
    else:
        print("The given expression is not a tautology\n")

def are_equivalent(ans1,ans2):
    if ans1 == ans2:
        print("Both expressions are logically equivalent")
    else:
        print("Expressions are not logically equivalent")

def fully():
    exp=input("Enter expression: ")
    p=[0,0,1,1]
    q=[0,1,0,1]
    vals=[]
    ops=[]
    #(p ⇒ q) ∨ (q ⇒ p) 
    k = len(exp)
    i=0
    while(i<k):
        j=0
        count=0
        if exp[i] =='(':
            #print("OOH bracket open \n")
            bracket_ulla = []
            brackops = []
            i+=1
            while(exp[i]!=')'):
                #print("Yo the inside values are ", exp[i])
                #print("I in WHILE = ",i)
                if exp[i]=='p':
                    bracket_ulla.append(p)
                elif exp[i] =='q':
                    bracket_ulla.append(q)
                else:
                    brackops.append(exp[i])
                i+=1
            #print("Ulla = ",eval(bracket_ulla,brackops))
            vals.append(eval(bracket_ulla,brackops))    
        if exp[i]=='p':
            vals.append(p)
        elif exp[i]=='q':
            vals.append(q)
            
        elif exp[i]==")":
            #print("Bracket close")
            pass
        else:
            ops.append(exp[i])
            #print("Operator = ",exp[i])
        #print("I in for = ",i)
        i+=1
        
    print(ops)
    print(vals)
    ans = eval(vals,ops)
    print("Answer is ",ans)
    
    print(ops)
    print(vals)   
    return ans     
    

r1 = fully()
is_tautology(r1)
r2 = fully()
is_tautology(r2)

are_equivalent(r1,r2)
