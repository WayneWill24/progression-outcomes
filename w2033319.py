 

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2033319
# Date: 20/11/2023

#student function
def student():

    ##While loop to loop until it output the final result 
    while True:
        ##To input Pass credits
        pass_Credits= input("\nEnter your PASS credits: ")

        #print out the output insend of an error if the input is not an number 
        try:
            pass_Credits= int(pass_Credits)
        except ValueError:
            print("\nInteger required\n*********************************") #(***) to make it easer for the user to read after every output  
            continue     #reset the loop to pass credits input

        #only accept numbers 0, 20, 40, 60, 80, 100, and 120 
        if pass_Credits != 0 and pass_Credits != 20 and pass_Credits != 40 and pass_Credits != 60 and pass_Credits != 80 and pass_Credits != 100 and pass_Credits != 120:
            print("\nOut of range\n*********************************")
            continue     #reset the loop to pass credits input


        ##To input Defer credits
        defer_Credits = input("\nNow enter your DEFER credits: ")

        #print out the output insend of an error if the input is not an number 
        try:
            defer_Credits = int(defer_Credits)
        except ValueError:
            print("\nInteger required\n*********************************")
            continue #reset the loop to pass credits input

        #only accept numbers 0, 20, 40, 60, 80, 100, and 120 
        if defer_Credits != 0 and defer_Credits != 20 and defer_Credits != 40 and defer_Credits != 60 and defer_Credits != 80 and defer_Credits != 100 and defer_Credits != 120:
            print("\nOut of range\n*********************************")
            continue #reset the loop to pass credits input


        ##To input Fail credits
        fail_Credits= input("\nAnd finally enter your Fail credits: ")

        #print out the output insend of an error if the input is not an number 
        try:
            fail_Credits= int(fail_Credits)
        except ValueError:
            print("\nInteger required\n*********************************") 
            continue #reset the loop to pass credits input

        #only accept numbers 0, 20, 40, 60, 80, 100, and 120 
        if fail_Credits != 0 and fail_Credits != 20 and fail_Credits != 40 and fail_Credits != 60 and fail_Credits != 80 and fail_Credits != 100 and fail_Credits != 120:
            print("\nOut of range\n*********************************") 
            continue #reset the loop to pass credits input


        ##To adds all 3 credits for the totel 
        totel_Credits = pass_Credits + defer_Credits + fail_Credits


        ##Finail outputs

        #this outputs if the totel is not 120
        if totel_Credits != 120:
            print ("\nTotal Incorrect\n*********************************")
            continue #reset the loop to pass credits input

        #this outputs if pass_Credits is 120
        elif pass_Credits == 120:
            print("\nProgress\n*********************************")
            break #break the loop and return to login input

        #this outputs if pass_Credits is 100
        elif pass_Credits == 100:
            print("\nProgress (module trailer)\n*********************************")
            break #break the loop and return to login input

        #this outputs if fail_Credits is 80
        elif fail_Credits >= 80:
            print("\nExclude\n*********************************") 
            break #break the loop and return to login input

        #this is defult output if totel_Credits is 120
        else:
            print("\nModule retriever\n*********************************") 
            break #break the loop and return to login input










#greeting
print("Hello")

### to input ether staff or student ether uppcase or lower
while True:
    login = input("\nTo Login as Student type 'Student' or 'student'. \nTo Login as Staff type 'Staff' or 'staff'.\n:") #(\n) to make it easer for the user to read 

###Student Login
    if login == "Student" or login == "student" :

        #student function call
        student()

    ###Staff Login
    elif login == "Staff" or login == "staff" :

        #To store progress students
        Progress = 0

        #To store trailer students
        Trailer = 0

        #To store retriever students
        Retriever = 0

        #To store exclude students
        Exclude = 0

        #To store the totle number of students
        totle_Students = 0

        #To store list of students results 
        student_List =[]

        ##While loop to loop until the user type q
        while True:

            #to input ether y or q ether uppcase or lower
            staff = input("\n\nType 'Y' or 'y' to enter a data\nType 'Q' or 'q'to quit\n: ")


            #print out the output if the input is not y or q ether uppcase or lower
            if staff != "y" and staff != "Y" and staff != "q" and staff != "Q" :
                print("\nThat's invalid\n*********************************")
                continue #reset the loop to staff input

            #break the loop when q or Q is enterd 
            elif staff == "q" or staff == "Q":
                break #break the loop and desplay the histogram, print the list and write the text file 

            ##To input Students Pass credits
            pass_Credits= input("\nPlease enter Student's PASS credits: ")

            #print out the output insend of an error if the input is not an number
            try:
                pass_Credits= int(pass_Credits)
            except ValueError:
                print("\nInteger required\n*********************************")
                continue #reset the loop to staff input

            #only accept numbers 0, 20, 40, 60, 80, 100, and 120 
            if pass_Credits != 0 and pass_Credits != 20 and pass_Credits != 40 and pass_Credits != 60 and pass_Credits != 80 and pass_Credits != 100 and pass_Credits != 120:
                print("\nOut of range\n*********************************")
                continue #reset the loop to staff input

            ##To input Students Defer credits
            defer_Credits = input("\nNow enter Student's DEFER credits: ")

            #print out the output insend of an error if the input is not an number
            try:
                defer_Credits = int(defer_Credits)
            except ValueError:
                print("\nInteger required\n*********************************")
                continue #reset the loop to staff input

            #only accept numbers 0, 20, 40, 60, 80, 100, and 120 
            if defer_Credits != 0 and defer_Credits != 20 and defer_Credits != 40 and defer_Credits != 60 and defer_Credits != 80 and defer_Credits != 100 and defer_Credits != 120:
                print("\nOut of range\n*********************************")
                continue #reset the loop to staff input

            ##To input Students Fail credits 
            fail_Credits= input("\nAnd finally enter Student's Fail credits: ")

            #print out the output insend of an error if the input is not an number
            try:
                fail_Credits= int(fail_Credits)
            except ValueError:
                print("\nInteger required\n*********************************")
                continue #reset the loop to staff input

            #only accept numbers 0, 20, 40, 60, 80, 100, and 120 
            if fail_Credits != 0 and fail_Credits != 20 and fail_Credits != 40 and fail_Credits != 60 and fail_Credits != 80 and fail_Credits != 100 and fail_Credits != 120:
                print("\nOut of range\n*********************************")
                continue #reset the loop to staff input

            ##To adds all 3 credits for the totel
            totel_Credits = pass_Credits + defer_Credits + fail_Credits

            #To store strngs while the loop is active 
            studentResults = ""

            #this outputs if the totel is not 120
            if totel_Credits != 120:
                print ("\nTotal incorrect\n*********************************")
                continue #reset the loop to staff input

            #this outputs if pass_Credits is 120
            elif pass_Credits == 120:

                #output this string to student_Results ones elif is executed 
                student_Results = f"\nProgress - {pass_Credits}, {defer_Credits}, {fail_Credits}"

                print("\nProgress\n*********************************")

                #couts everytime Progress is printed
                Progress += 1

            #this outputs if pass_Credits is 100
            elif pass_Credits == 100:

                #output this string to student_Results ones elif is executed 
                student_Results = f"\nProgress (module trailer) - {pass_Credits}, {defer_Credits}, {fail_Credits}"
                print("\nProgress (module trailer)\n*********************************")

                #couts everytime Trailer is printed
                Trailer += 1
                
            #this outputs if fail_Credits is 80
            elif fail_Credits >= 80:

                #output this string to student_Results ones elif is executed 
                student_Results = f"\nExclude - {pass_Credits}, {defer_Credits}, {fail_Credits}"
                print("\nExclude\n*********************************")

                #couts everytime Exclude is printed
                Exclude += 1

            #this is defult output if totel_Credits is 120
            else:

                #output this string to student_Results ones else is executed 
                student_Results = f"\nModule retriever - {pass_Credits}, {defer_Credits}, {fail_Credits}"
                print("\nModule retriever\n*********************************")

                #couts everytime Retriever is printed
                Retriever +=1

            #extend student_List with student_Results until the loop ends  
            student_List.extend([student_Results]) 

        # add the 4 results to get the totle number of students 
        totle_Students = Progress + Trailer + Retriever + Exclude

         



        # histogram
        from graphics import *   #import the graphics.py module (must be in the same folder this file)
         #OPEN THE WINDOW
        win = GraphWin("Student's Results", 800, 600)#open a window object called "win" with size and title 
        win.setBackground("black")# Set the background colour of the window



        #main heading
        heading= Text(Point(400, 30), " Student's Results")

        #heading styling
        heading.setStyle("bold")
        heading.setSize(35)
        heading.setTextColor("white")

        #opens in the window
        heading.draw(win) 
 


        #progress Rectangle
        progress_Rectangle = Rectangle(Point(100,480-Progress*10), Point(200,481)) #((Point(100,480-Progress)) - to minus the hight by the number of progress so the bar gose up  
        progress_Rectangle.setFill("green")

        #opens in the window
        progress_Rectangle.draw(win)


        #progress text
        progress = Text(Point(155,510),f"{Progress} \nProgress") #output totle number of progress students with the string

        #progress text styling
        progress.setTextColor("green")
        progress.setStyle("bold")
        progress.setSize(24)
        progress.setFace("helvetica")

        #opens in the window
        progress.draw(win)



        #trailer Rectangle
        trailer_Rectangle = Rectangle(Point(255,480-Trailer*10), Point(355,481)) #((Point(100,480-Trailer)) - to minus the hight by the number of trailer so the bar gose up
        trailer_Rectangle.setFill("yellow")

        #opens in the window
        trailer_Rectangle.draw(win)

        #progress text
        trailer = Text(Point(310,510),f"{Trailer} \nTrailer")#output totle number of trailer students with the string

        #trailer text styling
        trailer.setTextColor("yellow")
        trailer.setStyle("bold")
        trailer.setSize(24)
        trailer.setFace("helvetica")

        #opens in the window
        trailer.draw(win)



        #retriever Rectangle
        retriever_Rectangle = Rectangle(Point(410,480-Retriever*10), Point(510,481))#((Point(100,480-Retriever)) - to minus the hight by the number of retriever so the bar gose up
        retriever_Rectangle.setFill("orange")

        #opens in the window
        retriever_Rectangle.draw(win)


        #retriever text
        retriever = Text(Point(465,510),f"{Retriever} \nRetriever") #output totle number of retriever students with the string

        #retriever text styling
        retriever.setTextColor("orange")
        retriever.setStyle("bold")
        retriever.setSize(24)
        retriever.setFace("helvetica")

        #opens in the window
        retriever.draw(win)



        #exclude Rectangle
        exclude_Rectangle = Rectangle(Point(565,480-Exclude*10), Point(665,481))#((Point(100,480-Exclude)) - to minus the hight by the number of exclude so the bar gose up
        exclude_Rectangle.setFill("red")

        #opens in the window
        exclude_Rectangle.draw(win)

        #exclude text
        exclude = Text(Point(620,510),f"{Exclude} \nExcluded")#output totle number of exclude students with the string

        #exclude text styling
        exclude.setTextColor("red")
        exclude.setStyle("bold")
        exclude.setSize(24)
        exclude.setFace("helvetica")

        #opens in the window
        exclude.draw(win)


        #The line 
        aLine = Line(Point(50,482), Point(720,482))
        aLine.setFill("white")

        #opens in the window
        aLine.draw(win)



        #totle text
        totle = Text(Point(150,580),f"{totle_Students} student's in total") #output totle number of students with the string

        #totle text styling
        totle.setTextColor("white")
        totle.setStyle("bold")
        totle.setSize(18)
        totle.setFace("helvetica")

        #opens in the window
        totle.draw(win)




        #for loop that print the list line by line  
        for student_List in student_List:

            #write the list into a text file
            f=open("Student's Results.txt","a") #(a) it add new list into the text whale it is on loop 
            f.write(str(f"\n{student_List}"))
            f.close()

            #print out student_List
            print(student_List)
            
        break #break the loop and end system 


      #print this output if login input is not staff or student   
    else:
        print("\nInvalid input \n*********************************")



















