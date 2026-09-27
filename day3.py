marks1=int(input("Enter marks of English: "))
marks2=int(input("Enter marks of Math: "))
marks3=int(input("Enter marks of Chemistry: "))
marks4=int(input("Enter marks of Physics: "))

average=(marks1+marks2+marks3+marks4)/4
print("Average marks: ", average)


marks= int(input("Enter your mark: "))
if(marks<=70):
  grade="C"
  print(grade)

elif(marks>70 and marks<=80):
   grade="B"
   print(grade)

elif(marks>80 and marks<=90):
  grade="A"
  print(grade)

elif(marks>90 and marks<=100):
  grade="Outstanding"
  print(grade)

else:
  print("Fail")
