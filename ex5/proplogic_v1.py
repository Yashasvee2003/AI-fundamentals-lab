
p_or_q = [False,True,True,True]
p_and_q = [False,False,False,True]
p_implies_q = [True,True,False,True]
p_bidirec_q = [True,False,False,True]




input = "(p=>q)^(q=>p)v(p^q)"
simp = ""
ops = []
tables = []

def main():
    
    i = 0
    while i < len(input):
        # evaluate exp till ) 
        if input[i] == "(":
            j = input.find(")", i)
            # print(j)
            # find the operation used on the 2 atomic statements
            temp = input[i:j+1]
            tt = findTable(temp)
            tables.append(tt)
            i += (j-i+1)
        # store operator in ops array
        else:
            ops.append(input[i])

            i+=1
    print("content after simplifiying and obtaining tables")
    print(tables)
    print(ops)
    print("*********")

    # solving all tables
    while(len(ops)>=1 ):
        op = ops[0]
        temp =[]
        if op == '^':
            for i in range(4):
                temp.append(tables[0][i] and tables[1][i])
            tables[1] = temp
            tables.pop(0)
            ops.pop(0)
        elif op =='v':
            for i in range(4):
                temp.append(tables[0][i] or tables[1][i])
            tables[1] = temp
            tables.pop(0)
            ops.pop(0)
        print(tables)
        # print(ops,op)
    


def findTable(string):
    if "<=>" in string:
        return p_bidirec_q
    elif "=>" in string:
        if string[1] == 'p':
            return p_implies_q
        else:
            return p_implies_q[::-1]
    elif "^" in string:
        return p_and_q
    else:
        return p_or_q

if __name__== "__main__":
    main()

