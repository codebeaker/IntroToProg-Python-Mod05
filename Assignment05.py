# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sonu Mishra,5/12/25, edited script
# ------------------------------------------------------------------------------------------ #
#import json
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
student_data_unsaved: dict = {} #one row of unsaved student data
students_unsaved: list = [] # A table of unsaved student data


#Embed opening the json file and reading data in a try/except block
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
#Error handling for if the file does not exist
except FileNotFoundError as nofile: #using nofile instead of e to be less confusing
    if file.closed == False:
        file.close()
    print("JSON file must exist before running this script!\n")
    print("Built-in Python error info: ")
    print(nofile, nofile.__doc__, type(nofile), sep='\n')
#using 'generic_error' instead of e to be less confusing
#this is the generic exception
except Exception as generic_error:
    if file.closed == False:
        file.close()
    print("There was a non-specific error!")
    print("Built-in Python error info: ")
    print(generic_error, generic_error.__doc__, type(generic_error),
          sep='\n')



# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Option 1: Enable user to input data
    if menu_choice == "1":
        #Embed data input in try/except to maintain quality
        try:
            #Input the data
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should just be letters."
                                 "No Sus5an Smiths here.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should just be letters.")
            # Course name - can be alphanumeric but it's within the try block because
            # it's weird if you get an error and then get asked for course name
            course_name = input("Please enter the name of the course: ")

            # Add user input data to a list of dictionaries of unsaved data
            #This is within the try block, otherwise it will save bad data
            student_data_unsaved = {"FirstName": student_first_name,
                                    "LastName": student_last_name, "CourseName": course_name}
            students_unsaved.append(student_data_unsaved)
            print(f"You are registering {student_first_name} {student_last_name} "
                  f"for {course_name}.")
            print("Remember to save your data using Menu Option 3.")

        except ValueError as justalpha:
            print(justalpha)
            print("-- Technical Error Message --")
            print(justalpha.__doc__)
            print(justalpha.__str__())
            print("Try again")
        except Exception as generic_error:
            print("There was a non-specific error!")
            print("-- Technical Error Message --")
            print(generic_error, generic_error.__doc__, type(generic_error), sep='\n')
            print("Try again")



        #back to menu
        continue

    # Present the current data
    elif menu_choice == "2":

        # Display the data that is already saved
        print("The data that is already saved to file is:\n")
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled"
                  f" in {student["CourseName"]}.")
        print("-"*50)

        #Display the unsaved data if there is any
        if students_unsaved != []:
            print("The students you want to register in this session but "
                  "haven't saved to file yet are:")
            for student in students_unsaved:
                print(f"Student {student["FirstName"]} {student["LastName"]} for"
                      f" {student["CourseName"]}.")
            print("Remember to save this data using Menu Option 3.")
        else:
            print("There is no unsaved data at this time.")

        #Back to menu
        continue

    # Save the data to a file
    elif menu_choice == "3":

        # Tell the user if there is no unsaved data
        if students_unsaved == []:
            print("There is currently no unsaved data to save.")
        # Write unsaved data to file and inform user of what happened
        else:
            #Display the unsaved data that is being saved now
            print("The following new data is being saved to file:")
            for student in students_unsaved:
                print(f"Student {student["FirstName"]} {student["LastName"]} is "
                      f"enrolled in {student["CourseName"]}.")

            print("\nThe following data was saved to file previously:")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} is "
                      f"enrolled in {student["CourseName"]}.")

            # Add just-saved data to the main students list
            for student in students_unsaved:
                students.append(student)

            # Reset unsaved data structures to prevent dupes
            students_unsaved = []
            student_data_unsaved = {}

        # Write all the stored data to the file, overwriting the file so no dupes.
        #Embed it in a try-except block.
        ### Note this is out of the if/else above so it happens regardless of whether there is
        ### any unsaved data when the user hits 3
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file) #The elegant 'dump' function
            file.close()
            continue
        except TypeError as write_error:
            print("Please check that the data is a valid JSON format.\n")
            print("-- Technical Error Message --")
            print(write_error, write_error.__doc__, type(write_error), sep='\n')
        except Exception as generic_error:
            print("-- Technical Error Message --")
            print("Built-in Python error info: ")
            print(generic_error, generic_error.__doc__, type(generic_error),sep="\n")
        finally:
            if file.closed == False:
                file.close()

        # Return to the menu
        ### This code shouldn't run if the 'try' block above succeeds
        ### because that has 'continue' too
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
