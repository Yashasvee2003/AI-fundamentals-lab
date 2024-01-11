
# simpler version than the other
s= set()
def waterjug(three,four, p1,p2):
    if (three,four) not in s:
        print(three,four,"Paremts :: " ,p1,p2 ,end = "\n")
    s.add((three,four))

    if four ==2:
        print("Successssss")

    if three > 0 and (0, four) not in s:
        print("emptying 3l")
        waterjug(0, four, three, four)

        
    if three < 3 and (3, four) not in s:
        print("filling 3l")
        waterjug(3, four, three, four)

    if four > 0 and (three, 0) not in s:
        print("emptying 4l")
        waterjug(three, 0, three, four)

        
    if four < 4 and (three, 4) not in s:
        print("filling 4l")
        waterjug(three, 4, three, four)

    #4----> 3 Gallon		
    if three < 3 and four > 0:
        fillable = 3 - three
        # emptying 4G into 3G fully
        if fillable > four and (three + four, 0) not in s:  
            print("Fill 3 from 4 - non overflow") 
            # new_state = (three+four, 0)
            waterjug(three+four, 0, three, four)
        # usage of else messes up logic and gives negative results
        if fillable <= four:
            if (3, four - fillable) not in s:
                print("Fill 3 from 4 -  overflow")
                # new_state = (3 , four - fillable)
                waterjug(3, four- fillable, three, four)
    
    #3 ---> 4 Gallon
    if three > 0 and four < 4:
        fillable = 4- four
        # emptying 3G into 4G fully
        if fillable > three and (0,three+four) not in s:
            print("Fill 4 from 3 - non overflow")
            # new_state = (0,three+four)
            waterjug(0,three+four,three, four)
        # usage of else messes up logic and gives negative results
        if fillable <= three:
            if (three - fillable,4) not in s:
                print("Fill 4 from 3- overflow")
                # new_state = (three - fillable,4)
                waterjug(three - fillable,4,three, four)



waterjug(0,0,-1,-1)
print(s)
