def add_s(students):
    ''' Use to add students '''
    roll_no = int(input("Enter Roll No : "))

    if roll_no in [s[0] for s in students]: # Checks if the Student already exists with same roll no
        print("Roll No already assigned!")
        return

    name = input("Enter Name : ")
    father_name = input("Enter Student's Father Name : ")
    marks = int(input("Enter Student's Marks : "))
    grade = input("Enter Student's Grade : ")
    new_s=[roll_no,name,father_name,marks,grade] # new list for new student that be added
    students.append(new_s) # add the student at end in the student list

def remove_s(students):
    ''' Use to Remove students '''
    roll_no = int(input("Enter Roll No to be Removed : "))
    for s in students:                      # to iterate each student one by one
        if s[0] == roll_no : # to verify student
            students.remove(s)
    else:
        print("No Student Found!")

def all_s(students):
    ''' Use to Show all students '''
    for s in students: # prints all students
        print(s)

def average_s(students):
    ''' Use to display average students marks'''
    total = 0
    for s in students:
        total= total+ s[3] # Sum up the marks of each student at index 3
    total = total/len(students) # Averages the marks with number of all students
    print(total)

def min_s(students):
    ''' Use to show minimum marks students '''
    n_s=[] # New list for student marks only
    for s in students: # iterate to store all students marks in new list
        n_s.append(s[3]) # add all student marks
    n_ss=sorted(n_s) # sorts the list and stores it in new list
    print(students[n_s.index(n_ss[0])]) #fetches the index of the lowest marks and print the student of that index

def top_s(students):
    ''' Use to display top 3 students '''
    n_s = [] # New list for student marks only
    for s in students: # iterate to store all students marks in new list
        n_s.append(s[3])
    n_s.sort(reverse=True) # sorts list in decending order
    for s in n_s[0:3]: # fetches first three students
        print(students[n_s.index(int(s))]) #fetches the index of the lowest marks and print the student of that index

def service(): # Created to iterate the program multiple times!
    ''' Use to offer system services '''
    print("Choose the Service you want to Do :")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. All Students")
    print("4. Average of Students")
    print("5. Minimum Student")
    print("6. Top 3 Students")

    ch = int(input("Enter Choice : "))

    if ch == 1:
        add_s(students)
    elif ch == 2:
        remove_s(students)
    elif ch == 3:
        all_s(students)
    elif ch == 4:
        average_s(students)
    elif ch == 5:
        min_s(students)
    elif ch == 6:
        top_s(students)
    else:
        print("Invalid Choice")

students= [[1,"Ali","Zahid",86,"A"],[2,"Hamid","Zeshan",70,"B"],[3,"Abdullah","Amjad",90,"A"],[4,"Husnain","Shamir",56,"C"]] # Dummy database

print(":: Welcome to Student Management System ::")

while True:
    print("\n")
    service()
