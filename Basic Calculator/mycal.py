#import math module
import math
#while loop
while True:
#print the user option
	print("\nchoose the operation.\n\n0-add\n1-sub\n2-mul\n3-div\n4-modulo\n5-power\n6-square root\n7-log\n8-sine\n9-cosine\n10-tangent")
	#opiton selection
	oper=input("\nYour option")
	
	#add
	if oper=="0":
		v1 = float(input("\nFirst value: "))
		v2 = float(input("\nSecond value: "))
		
		print("\nthe result is :" +str(v1+v2)+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back	== "y":
			continue
		else:
			break
	#sub
	elif oper=="1":
		v1 = float(input("\nFirst value: "))
		v2 = float(input("\nSecond value: "))
		
		print("\nthe result is :" +str(v1-v2)+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
			
	#mul
	elif oper=="2":
		v1 = float(input("\nFirst value: "))
		v2 = float(input("\nSecond value: "))
		
		print("\nthe result is :" +str(v1*v2)+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
	
	#div
	elif oper=="3":
		v1 = float(input("\nFirst value: "))
		v2 = float(input("\nSecond value: "))
		
		print("\nthe result is :" +str(v1/v2)+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
			
	#modulo
	elif oper=="4":
		v1 = float(input("\nFirst value: "))
		v2 = float(input("\nSecond value: "))
		
		print("\nthe result is :" +str(v1%v2)+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
	
	#power
	elif oper=="5":
		v1 = float(input("\nFirst value: "))
		v2 = float(input("\nSecond value: "))
		
		print("\nthe result is :" +str(math.pow(v1,v2))+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
	#sqrt
	elif oper=="6":
		v1 = float(input("\nEnter the value for square root: "))
		
		print("\nthe result is :" +str(math.sqrt(v1))+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
			
	#log
	elif oper=="7":
		v1 = float(input("\enter the value: "))
		
		print("\nthe value for log base :" +str(math.log(v1,2))+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
			
	#sine
	elif oper=="8":
		v1 = float(input("\nenter the value(in degree): "))
		
		print("\nthe value for sin :" +str(math.sin(math.radians(v1)))+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
		
	#cos
	elif oper=="9":
		v1 = float(input("\nenter the value(in degree): "))
		
		print("\nthe value for cos :" +str(math.cos(math.radians(v1)))+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
			
	#tan
	elif oper=="10":
		v1 = float(input("\nenter the value(in degree): "))
		
		print("\nthe value for tan :" +str(math.tan(math.radians(v1)))+"\n")
		#go back to main menu or exit 
		back = input("\ngo back to the menu (y/n)")
		
		if back == "y":
			continue
		else:
			break
			
	#handling invalid input
	else:
		print("\nInvalid option!\n")
		continue
	#end of pgm