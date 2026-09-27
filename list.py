## Data Structure ##
# List is mutable
students=["Amit","Rahul","Priya","Neha", "Ram", "Sakshi", "Shreya"]
print(students[2])     #indexing
print(students[-1])    #slicing
print(students[2::4])
print(students[1:2])

students.append("Sai")   #append
print(students)

students.insert(2,"Ruhi")  #insertion
print(students)

students.remove("Ram")  #remove
print(students)

students.pop()    #pop
print(students)

a=len(students)
print(a)  #length

students.sort()
print(students)       #sort

print(students.reverse())   #reversing    # only perform on string


#Next
marks=[23, 45, 80, 70, 50, 30, 50, 90, 40]  # Element changing
marks[1]=100
print(marks)

x=marks.append(123)   ##append
print(marks)

y=marks.insert(1, 55)  ##insert
print(marks)

z=marks.remove(90)    ##Remove
print(marks)

marks.pop()     ##Pop
print(marks)

marks.pop(1)
print(marks)

print(len(marks))  ## length