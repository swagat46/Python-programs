import os

filename = "students.txt"

try:
    #1.CREATE NEW FILE
    with open(filename, "x") as file:
        file.write("Name:Yogesh\n")
        file.write("Course:Python\n")
        file.write("Age:25\n")
    print("1.File created successfully.")


    #2.WRITE OPERATION
    with open(filename,"w") as file:
        file.write("Name:Yogesh\n")
        file.write("Course:Python Django\n")
        file.write("City:Pune\n")

    print("2.Data written successfully")


    #3.READ COMPLETE FILE
    with open(filename, "r") as file:
        data=file.read()

    print("\n3.Complete File Data: ")
    print(data)

    #4.READ ONE LINE
    with open(filename,"r") as file:
        line=file.readline()

    print("4.First line: ")
    print(line)

    #5.READ ALL LINES
    with open(filename, "r") as file:
        lines=file.readlines()

    print("5.All Lines: ")
    print(lines) 

    #6.APPEND OPERATION 
    with open(filename,"a") as file:
        file.write("Technology:Python\n")
        file.write("Experience:2.5 Years\n")

    print("6.Data Appended Successfully")

    #7.READ UPDATED FILE
    with open(filename,"r") as file:
        print("\n 7.Updated file data:")
        print(file.read())


    #8.CHECK FILE EXISTS
    if os.path.exists(filename):
        print("8.File Exists")


    #9.FILE INFORMATION
    size=os.path.getsize(filename)

    print("9.File Size:",size,"bytes")

except FileExistsError:
    print("File Already Exists")

except FileNotFoundError:
    print("File Not Found")

except Exception as e:
    print("Error:", e)


    #10.DELETE FILE
    if os.path.exists(filename):
        os.remove(filename)
        print("10.File Deleted Successfully")
        

           




       