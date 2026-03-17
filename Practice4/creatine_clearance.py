# Use input() function to get user inputs
# Convert age to integer, weight/creatinine to float
# Gender is kept as string for validation

try:
    # Get inputs from user
    age_input = input("Enter age (years): ")
    weight_input = input("Enter weight (kg): ")
    gender_input = input("Enter gender (male/female): ")
    cr_input = input("Enter creatinine concentration (umol/l): ")

    # Convert inputs to correct data types
    age = int(age_input)
    weight = float(weight_input)
    gender = gender_input.strip().lower()  # Normalize gender input (remove spaces, lowercase)
    creatinine = float(cr_input)

except ValueError:
    # Handle case where conversion fails (e.g., text entered for number)
    print("\nError: Invalid input type. Please enter numeric values for age, weight, and creatinine.")
    exit()  # Terminate program if conversion fails

# Check each input against specified ranges/conditions
# Collect error messages to display all issues at once

error_messages = []

# Validate age
if age >= 100:
    error_messages.append(f"Age '{age}' is invalid. Must be less than 100.")

# Validate weight (20 < weight < 80)
if not (20 < weight < 80):
    error_messages.append(f"Weight '{weight}' kg is invalid. Must be between 20 and 80 kg.")

# Validate creatinine concentration (0 < Cr < 100)
if not (0 < creatinine < 100):
    error_messages.append(f"Creatinine '{creatinine}' umol/l is invalid. Must be between 0 and 100.")

# Validate gender
if gender not in ['male', 'female']:
    error_messages.append(f"Gender '{gender}' is invalid. Please enter 'male' or 'female'.")

# If no errors, calculate CrCl; otherwise, show validation errors
if not error_messages:
    # Cockcroft-Gault Equation: CrCl = ((140 - age) * weight) / (72 * creatinine)
    # Multiply by 0.85 if female
    crcl = ((140 - age) * weight) / (72 * creatinine)
    
    # Apply female correction factor
    if gender == 'female':
        crcl *= 0.85

    # Display results with clear formatting
    print("\n=== Creatinine Clearance Calculation Result ===")
    print(f"Patient Age: {age} years")
    print(f"Patient Weight: {weight} kg")
    print(f"Patient Gender: {gender}")
    print(f"Creatinine Concentration: {creatinine} umol/l")
    print(f"Estimated CrCl: {crcl:.2f} ml/min")  # Format to 2 decimal places

else:
    # Display all validation errors (use str() to convert list to string for output)
    print("\n=== Input Validation Errors ===")
    # str() converts the list of errors into a readable string
    print(str("\n".join(error_messages)))






#变量
#age = int(input("please provide your age(years)："))
#while age>=100:
#	print ("age needs correcting")
#	break
#else:
#	weight = float(input("please provide your weight(kg)："))
#	while  weight<=20 or weight>=80:
#		print ("weight needs correcting")
#		break
#	else:
#		gender = input("please provide yourgender(male/female)：")
#		while gender!="male" and gender!="female":
#			print("gender needs correcting")
#			break 
#		else :
#			conCr = float(input("please provide your creatine concentration(mg/dL)："))
#			while conCr<=0 or conCr>=100:
#				print ("creatine concentration needs correcting")
#				break
#			
#			break
#		break
#	break 
#
#else:
	#height = int(input("please provide your height(cm)：")) 
#	CrCl=0
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
#	if gender == "female":
#		CrCl = ((140 - age) * weight * 0.85) / (72 * conCr)
#		print("the creatine clearance (CrCl)is：",CrCl," mL/min")
#	else:
#		CrCl = (140 - age) * weight / (72 * conCr)
#		print("the creatine clearance (CrCl)is：",CrCl," mL/min")

# output
