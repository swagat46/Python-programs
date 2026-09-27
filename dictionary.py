Student= {
    "name":"abc",
    "age":22,
    "collage":"SIT",
    "marks":99,
}

print(Student["name"])
print(Student["age"])

Student["marks"]=80     # REplace
Student["age"]=23
print(Student)

print(Student.values())   #values
print(Student.keys())     #Keys
print(Student.get("age")) #get
print(Student.items())    #items

   ## Next
                           # Nested Structure
students= [
    {"name":"xyz", "age":34, "maek":80},
    {"name":"abc", "age":20, "mark":"90"},
    {"name": "def", "age":22, "mark":95}
]

print(students[0]["name"])
print(students[2]["mark"])