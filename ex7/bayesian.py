def pr(exam):
	for i in exam:
		if exam[i]==0:
			for j in i:
				print(j,end="\t")
			print()
		else:
			k=len(i)
			for l in range(k):
				print(i[l],end="\t")
			print(exam[i])


exam={("exam","value"):0,(0,):0.7,(1,):0.3}
iq={("iq","value"):0,(0,):0.8,(1,):0.2}
marks={("iq","exam","mark","value"):0,(0,0,0):0.6,(0,0,1):0.4,(0,1,0):0.9,(0,1,1):0.1,(1,0,0):0.5,(1,0,1):0.5,(1,1,0):0.8,(1,1,1):0.2} #iq,exam,mark
apti={("iq","apti","value"):0,(0,0):0.75,(0,1):0.25,(1,0):0.4,(1,1):0.6} #iq,apti
admi={("marks","value"):0,(0,0):0.6,(0,1):0.4,(1,0):0.9,(1,1):0.1} #mark

data=[exam,iq,marks,apti,admi]
final=1
for i in data:
	pr(i)
	li=list(i)
	final*=i[li[-1]]
print("Bayesian probability : ",final)
#print(len(exam))
#print(list(exam))
