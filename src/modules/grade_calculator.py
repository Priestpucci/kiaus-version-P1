#2025 A LEVEL grade Boundaries 
grade_boundaries = []

choice = input( "select method of calculation: (calculate Grade | 1 ) , (Calculate Percentage | 2) , (Calculate Grade & Percentage | 3) ")

def Calculate_percentage(score):
  total_mark = float(input("Total Marks In Paper: "))
  P =  (round((score/total_mark) * 100))
  return P

def Grade(score):
  for i in range(6):
    while True:
        num = int(input(f"enter singular lower boundary in descending order of each grade value): "))# Lower Boundaries: A*, A , B , C ,D ,E 

        if grade_boundaries and num >= grade_boundaries[-1]:
           print("Invalid input | Lower grade boundary is greater than previous inputted value; try again.")
    
        else:
          grade_boundaries.append(num)

  print("Lower boundary of each grade | ", grade_boundaries)     
  if score >= grade_boundaries[0]:
        return 'A*'
  elif score >= grade_boundaries[1]:
        return 'A'
  elif score >= grade_boundaries[2]:
        return 'B'          # need to fix 
  elif score >= grade_boundaries[3]:
        return 'C'
  elif score >= grade_boundaries[4]:
        return 'D'
  elif score >= grade_boundaries[5]:
        return 'E'
  else:
        return 'U'
         
score = int(input("Enter the appropriate mark the student obtained out of Total: "))

if choice == "1":
     Student_grade = Grade(score)
     print(f'student obtained | {Student_grade}')

elif choice == "2":
     Student_percentage = Calculate_percentage(score)
     print(f'student obtained | {Student_percentage}%')
     
elif choice == "3":
     Student_grade = Grade(score)
     Student_percentage = Calculate_percentage(score)
     print (f'Student Percentage & Grade: {Student_percentage}% | {Student_grade}')
    
   
     
    
# NEED TO CREATE A  NAME SYSTEM; CAN ALLOCATE BOTH GRADES AND PERCENTAGES TO A STUDENT AND SAVE IT INTO A DATABASE
# CSV FOR EXCEL DATABASE TO MAKE IT USER FRIENDLY AND ACCESIBLE 
#NEED TO BE ABLE TO DO BOTH FOR A STUDENT 
# DATABSE MUST BE ABLE TO STORE ALL OF STUDENTS DATA AND PROGRESSION 

    



 