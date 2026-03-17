#变量
age = int(input("please provide your age(years)："))
while age>=100:
	print ("age needs correcting")
	break
else:
	weight = float(input("please provide your weight(kg)："))
	while  weight<=20 or weight>=80:
		print ("weight needs correcting")
		break
	else:
		gender = input("please provide yourgender(male/female)：")
		while gender!="male" and gender!="female":
			print("gender needs correcting")
			break 
		else :
			conCr = float(input("please provide your creatine concentration(mg/dL)："))
			while conCr<=0 or conCr>=100:
				print ("creatine concentration needs correcting")
				break
			
			break
		break
	break 

else:
	#height = int(input("please provide your height(cm)：")) 
	CrCl=0
	#判断data是否合理
	#if age>=100:
	#    print ("age needs correcting")

	#if  weight<=20 or weight>=80:
	#	print ("weight needs correcting")

	#if conCr<=0 or conCr>=100:
	#	print ("creatine concentration needs correcting")
	#if gender!="male" and gender!="female":
	#	print("gender needs correcting")
	# the equation
	#"female"
	if gender == "female":
		CrCl = ((140 - age) * weight * 0.85) / (72 * conCr)
		print("the creatine clearance (CrCl)is：",CrCl," mL/min")
	else:
		CrCl = (140 - age) * weight / (72 * conCr)
		print("the creatine clearance (CrCl)is：",CrCl," mL/min")

# output
