import linecache
import statistics

def showing_option():
	print ("Press 1: To showing Data ")
	print ("Press 2: Count The number of students in file ")
	print ("Press 3: Compute Final score")
	print ("Press 4: Compute and Show Grade")
	print ("Press 5: Column Statistics ")
	print ("Press 6: Show students of grade A")
	print ("Press 7: Search by name")
	print ("Press 8: Exit ")
	print ("--->Enter Choice : ")


#//////////////////////////////////////////////////////////////////////////////
#Part of showing Data


print("----WELCOME TO MY PROGRAM GRADE----",'\n')

with open("Cstudents.csv", "r") as f:
    score = f.read() # Read all file in case values are not on a single line
    
    
    #-----------user choice------
    showing_option()
    user = input(str())
    
    #------------------------------
    score_final= [ int(x) for x in score.split()[2: :4]]
    score_mid = [  int (x) for x in score.split()[1: :4]]
    score_id = [  int (x) for x in score.split()[3: :4]]
    score_name = [  str (x) for x in score.split()[0: :4]]
    score_total = [x + y for x, y in zip(score_mid, score_final)]
    
    if (user == "1"):
    	print ("----NOTE : this data is Displayed in order----")
    	print ("Names of students: ",score_name,'\n')
    	print("Grades of Midterm: ",score_mid,'\n')
    
    	print ("Grades of Final: ",score_final,'\n')
    	print ("ID of students : ", score_id,'\n')

#/////////////////////////////////
#//////////Part of count student

    elif (user == "2"):
    	print (" Number of Students is : " ,len(score_name), "Students.")
    	
#//////////////////////////////////////////
#Part of final score
    elif (user == "3"):
    	for x in score_total:
    		inf = score_total.index(x)
    		print ("Name : ", score_name[inf])
    		print ("The final score is : ", score_total[inf])
#//////////////////////////////////
    #Part of stat
    if (user == "5"):
    	print ("Minimum Score is: ",min(score_total))
    	print ("Maximum Score is: ", max (score_total))
    	print ("The Average is : ", statistics.mean(score_total))
    	print("Variane of Data is : ", statistics.variance(score_total))
    	print("Standard deviation of Data is : ", statistics.stdev(score_total))
  
#///////////////////////////////////////////
    	
    #part of Grade
    elif (user == "4"):
    	for x in score_total:
    		if 100>= x >=90:
    			fir = score_total.index(x)
    			print ("Name: " , score_name [fir], ", ID : ", score_id[fir], ", Points is: ", x, ", Your Grade is A ")
    		
    		if 90> x>=75:
    			sec = score_total.index(x)
    			print ("Name: " , score_name [sec], ", ID : ", score_id[sec], ", Points is: ", x, ", Your Grade is B ")
    			
    			
    		if 75> x >=60:
    			thi = score_total.index(x)
    			print ("Name: " , score_name [thi], ", ID : ", score_id[thi], ", Points is: ", x, ", Your Grade is C ")
    			
    		if 60>x>=50:
    			fort = score_total.index(x)
    			print ("Name: " , score_name [fort], ", ID : ", score_id[fort], ", Points is: ", x, ", Your Grade is D ")
    			
    			
    		if (50> x):
    			fif = score_total.index(x)
    			print ("Name: " , score_name [fif], ", ID : ", score_id[fif], ", Points is: ", x, ", Your Grade is F ")
    			
 
#//////////////////////////////////////////////////////////////////////////////Part of Grade A stu

    elif (user == "6"):
    		for x in score_total:
    			if 100>= x >=90:
    				ind = score_total.index(x)
    				print (score_name[ind], " your grade is A : ", x)
  
  
  
#//////////////////////////////////////////////////////////////////////////////Part of Search 

    elif (user == "7"):
    	print ("  Ok ! please enter the name of search: ")
    	src = input(str())
    	for x in score_name :
    		if (src == x):
    			fon = score_name.index(x)
    			print ("Your name is: ", score_name[fon])
    			print (" ID is : ",score_id[fon])
    			print ("Coursework is : ",score_mid[fon])
    			print ("Final  is : ",score_final[fon])
    			print ("Total grade is : ",score_total[fon])
    			break;
    	else :
    		print (" This Student is not found")
 #////////////////////////////////////////////#Part of Exit
 
#print ("--------------------------------------------")
    elif (user == "8"):
    	print (" OK ^_^ ! see you next time")
    	
    