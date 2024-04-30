class Student:
    def __init__(self,name,rollNO,marks1,marks2,passW):
        self.name = name
        self.rollNO = rollNO
        self.marks1 = marks1
        self.marks2 = marks2
        self.passW = passW

    @classmethod
    def acceptStudentDetails(cls,name,rollNO,marks1,marks2,passW):
        ob = cls(name,rollNO,marks1,marks2,passW)
        l.append(ob)

    def displayTable(self,l):
        print("No.\tName\tRollNo\tMarks1\tMarks2\tPassWord")
        for i in range(l.__len__()):
            print(i+1,".\t",l[i].name,"\t",l[i].rollNO,"\t",l[i].marks1,"\t",l[i].marks2,"\t",l[i].passW)

    def search(self,rn):
        for i in range(l.__len__()):
            if(l[i].rollNO == rn):
                return i
    
    def display(self,o):
        print("Name:",o.name)
        print("RollNo:",o.rollNO)
        print("Marks1:",o.marks1)
        print("Marks2:",o.marks2)
        print("PassWord:",o.passW)
        print("\n")

    def delete(self,rn):
        i=obj.search(rn)
        del l[i]

    def update(self,rn,No):
        i=obj.search(rn)
        roll = No
        l[i].rollNO = roll


l = []
obj = Student("",0,0,0,0)

obj.acceptStudentDetails("A",1,45,45,'123')
obj.acceptStudentDetails("B",2,45,45,'456')
obj.acceptStudentDetails("C",3,45,45,'789')

while True:
    print("1.Teachers Login\n2.Student Login\n3.Exit")
    loginChoice = input("Enter Choice:-")
    if loginChoice == '1':
        teacherUserID = "Teacher"
        teacherPassword = "4567"

        choiceUserID = input("Enter USerID:-")
        if choiceUserID == teacherUserID:
            choicePassword = input("Enter Password:-")
            if choicePassword == teacherPassword:
                print("login Successfull")
                while True:
                    print("Teachers Login SuccessFull \n------------------------")
                    print("\n1.Accept Student details \n2.Display Student details \n3.search details of a Student \n4.Delete Details of student\n5.Update student Details \n6.Exit")
                    tChoice = input("Enter Choice")
                    if tChoice == '1':
                        while True:
                            print("Accept Student Detail")
                            name = input("Enter Name:-")

                            while True:
                                rollNO = input("Enter RollNO:-")
                                if rollNO.isdigit() == True:
                                    rollNO = int(rollNO)
                                    break
                                else:
                                    print("Invalid Input Try Again!!!!")

                            while True:
                                marks1 = input("Enter marks1:-")
                                if marks1.isdigit() == True:
                                    marks1 = int(marks1)
                                    break
                                else:
                                    print("Invalid Input Try Again!!!!")
                            
                            while True:
                                marks2 = input("Enter marks2:-")
                                if marks2.isdigit() == True:
                                    marks2 = int(marks2)
                                    break
                                else:
                                    print("Invalid Input Try Again!!!!")

                            passW =input("Enter PassWord:-")

                            obj.acceptStudentDetails(name,rollNO,marks1,marks2,passW)

                            for i in range(l.__len__()):
                                print(l[i].name)
                                print(l[i].rollNO)
                                print(l[i].marks1)
                                print(l[i].marks2)
                                print(l[i].passW)

                            print("1.Enter New Entry\n2.Exit")
                            ch1 = input("Enter Choice")
                            if ch1 == '1':
                                continue
                            elif ch1 == '2':
                                print("Thank You!!!")
                                break
                            else:
                                print("Invalid INPUT!!!!!")
                                break
                    elif tChoice == '2':
                        print("Display Student Detail")
                        print("\nList of students\n")
                        
                        obj.displayTable(l)
                        print("1.Want See Again..\n2.Exit")
                        nExit = int(input("Enter Choice:-"))
                        if nExit==2:
                            break

                    elif tChoice == '3':
                        print("Search Student Detail")
                        while True:
                                n=input("Enter student Roll No")
                                while True:
                                    if n.isdigit():
                                        n = int(n)
                                        break
                                    else:
                                        print("Invalid Input,Try Again!!!")

                                for i in range(l.__len__()):
                                    if n == l[i].rollNO:
                                        print("\n Student Found")
                                        s = obj.search(n)
                                        obj.display(l[s])
                                    
                                print("1.Want to see another student data\n2.Exit")
                                nExit = int(input("Enter Choice:-"))
                                if nExit==2:
                                    break
                    elif tChoice == '4':
                        print("Delete Student Detail")
                        while True:
                                while True:
                                    n=input("Enter student Roll No:-")
                                    if n.isdigit():
                                        n = int(n)
                                        break
                                    else:
                                        print("Invalid Input,Try AGAIN!!!!")
                                obj.delete(n)
                            
                                print("List after deletion")
                                for i in range(l.__len__()):
                                    obj.display(l[i])
                                obj.displayTable(l)
                                print("1.Want to delete another student data\n2.Exit")
                                nExit = int(input("Enter Choice:-"))
                                if nExit==2:
                                    break
                    elif tChoice == '5':
                        print("Update Student Detail")
                        while True:
                                n=int(input("Enter student Roll No"))
                                nr=int(input("Enter New Roll Number:"))
                                obj.update(n,nr)
                                print(l.__len__())
                                print("List after updation")
                                for i in range(l.__len__()):
                                    obj.display(l[i])
                                print("1.Want to update another student data\n2.Exit")
                                nExit = int(input("Enter Choice:"))
                                if nExit==2:
                                    break
                    elif tChoice == '6':
                        print("Exit")
                        break
            else:
                print("wrong PassWORD")
        else:
            print("Invalid USerID Try Again!!!")

    elif loginChoice == '2':
        print("Student Login")
        while True:

                userID=input("Enter UserID/Name:-")
                for i in range(l.__len__()):
                    if l[i].name == userID:
                        passWS = input("Enter Password:-")
                        
                        for i in range(l.__len__()):
                            if  l[i].passW == passWS:
                                """Student Login"""
                                while True:
                                    # n=int(input("Enter student Roll No"))
                                    rni = l[i].rollNO
                                    print("\n Student Found")
                                    s = obj.search(rni)
                                    obj.display(l[s])
                                    break
                print("1.Want to view Again\n2.Exit")
                nExit = input("Enter Choice:-")
                if nExit=='2':
                    break
                elif nExit == '1':
                    pass
                else:
                    print("Invalid Choice")
                    break
                
    elif loginChoice == '3':
        print("ExitLogin")                                                 
        break
    else :
        print("Invalid INput TRy AGaian!!!!!!")