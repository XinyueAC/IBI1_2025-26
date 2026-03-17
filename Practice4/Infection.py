#1.difine variables: the number of days and the initial number of infected people
ini=5
j=0  #days counter

#2.Use a while loop to calculate the number of days until the number of infected people reaches 91 or more, assuming the number of infected people increases by 40% each day.
while ini<91:
	ini=1.4*ini
	j+=1
while ini>=91:
	break
print (j,"days")


