#2025 A LEVEL grade Boundaries 
grade_boundaries = []

def Calculate_percentage(score):
  total_mark = float(input("Total Marks In Paper: "))
  P =  (round((score/total_mark) * 100))
  print(f"Student percentage | {P}%")

def Grade(score):
  for i in range(6):
      grade_boundaries.append(int(input(f"enter singular lower boundary in descending order of each grade ({i+1} value): "))) # Lower Boundaries: A*, A , B , C ,D ,E 

  print("Lower boundary of each grade | ", grade_boundaries)

  if score >= grade_boundaries[0]:
      print('student obtained | A*')
  elif score >= grade_boundaries[1]:
      print('student obtained | A')
  elif score >= grade_boundaries[2]:
      print('student obtained | B')           # need to fix 
  elif score >= grade_boundaries[3]:
      print('student obtained | C')
  elif score >= grade_boundaries[4]:
      print('student obtained | D')
  elif score >= grade_boundaries[5]:
      print('student obtained | E')
  else:
      print('student obtained | U')
         
score = int(input("Enter the appropriate mark the student obtained out of Total: "))
choice = input( "select method of calculation: (calculate Grade | 1 ) , (Calculate Percentage | 2) , (Calculate Grade & Percentage | 3) ")

if choice == "1":
    Grade(score)
elif choice == "2":
    Calculate_percentage(score)
elif choice == "3":
    Grade(score) 
    Calculate_percentage(score)
    
# NEED TO CREATE A  NAME SYSTEM; CAN ALLOCATE BOTH GRADES AND PERCENTAGES TO A STUDENT AND SAVE IT INTO A DATABASE
# CSV FOR EXCEL DATABASE TO MAKE IT USER FRIENDLY AND ACCESIBLE 
#NEED TO BE ABLE TO DO BOTH FOR A STUDENT 
# DATABSE MUST BE ABLE TO STORE ALL OF STUDENTS DATA AND PROGRESSION 

    



 