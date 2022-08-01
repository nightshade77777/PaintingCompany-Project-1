# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:31:44 2022

@author: SUHAANI
"""

'''

Display a title stating “Employee details”.
• Ask the user to enter the employee’s ID, name, telephone number.
• Ask the user to enter the employee’s qualification level using the codes:
• AP for apprentice
• FQ for fully-qualified.
• Display the employee details on the screen:
• If the user entered AP in the qualification level, it should display it as “Apprentice”,
if they entered FQ it should display as “Fully-qualified”. 
If any other data is entered it should display an error message.
• Ask the user to confirm the information is correct:
• If any information is incorrect, ask the user to re-enter all of the data again and
then display the employee details again.
• Return to the title message.
'''

#TASK 1 - employee details 
print()
print("EMPLOYEE DETAILS ")
print()

def details():
    #ask user 
    employee_id = input("Enter your employee ID: ")
    employee_name = input("Enter your name: ")
    employee_num = int(input("Enter your phone number: "))

    #validate employee code
    validated = "false"
    while validated == "false":
        print("Employee qualification code")
        print()
        print("[AP]: Apprentice or [FQ]: Fully Qualified. ")
        
        employee_quali = input("Please enter: ")
        print()
        if employee_quali == "ap" or employee_quali == "AP":
            print("Apprentice ")
            validated = "true"
            
        elif employee_quali == "fq" or employee_quali == "FQ":
            print("Fully Qualified ")
            validated = "true"
            break
            
        else:
            print("Try again. ")
            print()
    
    #confirm details
    print()
    print("Please enter 'C' if all your details are correct. ")
    print("Please enter 'N' if you would like to re-enter your details incase of an error. ")
    print()
    
    confirmation = input("Confirm: ")
    confirmation.upper()

    repeat = "false"
    
    #validate confirmation
    while repeat == "false":
        if confirmation == "C" or confirmation == "c":
            print("Thank you! ")
            print()
            print("EMPLOYEE DETAILS: ")
            print(employee_name)
            print(employee_id)
            print(employee_num)
            print(employee_quali)
            print()
            repeat = "true"
            break
        elif confirmation == "N" or confirmation == "n":
            details()
            repeat = "true"
            break
        
        else:
            print("Try again. ")
            
details()
print()

'''

Display a welcome message.
• Ask the user for this information:
• Customer number, date of estimate, number of rooms that require painting:
• For each room, ask for the room name (e.g. lounge, dining room) 
and the number of walls in the room:    
    • Ask if wallpaper needs to be removed – if yes, charge £70 per room
   • For each wall, ask the height and width of the wall in metres.
• Calculate the total surface area of the walls in square metres.
• Multiply the total surface area of the walls by £15 per square metre for paint.
• Ask what type of employee should be assigned to the job.
• Add on the cost of the employee – if apprentice add on £100, if fully-qualified add
on £250.
• Calculate and display the total.
• Add 20% VAT to the total.
• Calculate and display the final total.
• Ask the user if they wish to generate another estimate:
• If yes, return to the welcome message
• If no, display an exit message.

'''
    
#TASK 2 - Generating estimates
cost = 0 
wpaper_cost = 0
WALLPAPER_REMOVING = 70
PAINT_COST = 15
surface_area = 0 
paint_sa = 0 
AP = 100 
FQ = 250 
VAT = 0.2


customer_num = input("Please enter your customer number: ")
date_of_est = input("Please enter the date of estimate: ")
num_of_rooms = int(input("Please enter the number of rooms that require painting: "))
print()

#asking for number of rooms and number of walls in each room
if num_of_rooms != 0:
    for i in range(num_of_rooms):
        room_name = input("Please enter the room name: ")
        num_of_walls = int(input("Please enter the number of walls in the room: "))
else:
    print("Alright, moving on! ")

#validation check for wallpaper removal
flag = "false"
while flag == "false":
    #asking if user needs a wallpaper
    print("It costs 70$ per room to remove the wallpaper. ")
    wallpaper_option = input("Please enter 'Y' if you want the wallpaper to be removed or 'N' to keep them: ")
    if wallpaper_option == "y" or wallpaper_option == "Y":
        #if yes, add to cost
        wpaper_cost = num_of_walls * WALLPAPER_REMOVING
        flag = "true"
        
    elif wallpaper_option == "n" or wallpaper_option == "N":
        print("Got it, thanks! ")
        flag = "true"
        
    else:
        print("Invalid input, please try again. ")

#asking height and width for each wall
for i in range(num_of_walls):
    height = int(input("Please enter the height of the wall in metres: "))
    width = int(input("Please enter the width of the wall in metres: "))

#calculating SA and multiplying it with paint cost     
surface_area = height * width
paint_sa = surface_area * PAINT_COST
print("It will cost you ", paint_sa, " to paint your room. ")
print()

#adding it to total cost
cost = cost + paint_sa + wpaper_cost 

print("We have 2 types of employees: [AP] Apprentice and [FQ] Fully Qualified.  ")
print()
print("It will cost you 100$ if you choose Apprentice and 250$ if you choose Fully Qualified. ")

check = "false"

#validation check and asking user about type of employee qualification 
while check == "false":
    type_of_emp = input("Please enter which employee qualification level you want for the job: ")
    
    if type_of_emp == "AP" or type_of_emp == "ap":
        cost += AP
        print("That's great! Thank you. ")
        check = "true"
        break
    
    elif type_of_emp == "FQ" or type_of_emp == "fq":
        cost+= FQ
        print("That's great! Thank you. ")
        check = "true"
        break
    
    else:
        print("Invalid input. Try again. ")
        
#total cost
vat_price = cost * VAT
cost = cost + vat_price
print("Your total cost is: ", cost, "$")
print()

'''
The program will sort and search the file paintingJobs.txt to select and display
information about estimates and jobs.

The paintingJobs.txt file shows Estimate Number, Estimate Date, Customer ID,
Final Total (in £ pounds), Status (E for Estimate, A for Accepted job or N for Not accepted),
and Amount Paid (in £ pounds). 

REQUIREMENTS:
• Display four options for the user to select from.
Option A Search for an estimate
Option B Display outstanding payments
Option C Display total revenue
Enter Q to quit
• The user must be able to select an option or enter ‘Q’ to quit the program.
• All data must be read from the paintingJobs.txt file.
• The program must work for all of the records in the paintingJobs.txt file.


'''

#displays a menu for user to choose from
def menu():
    print("[A] Option A: Search for an estimate ")
    print("[B] Option B: Display outstanding payments ")
    print("[C] Option C: Display total revenue ")
    print("[Q] Option Q: Quit ")

menu()

#main program is broken down into subprograms for better readibility 

#OPTION A 
'''
Option A must provide a prompt for the user to enter the estimate number.
• It must find the customer ID and estimate details for the entered estimate number.
• Here is a suggested format for displaying the data.
Estimate Number: <the estimate number>
Customer ID: <the customer ID>
Estimate Amount: <the final total>
Estimate Date: <the estimate date>
Status: <the status>

'''
def optionA():
    myfile = open("paintingjobs.txt", "r")
    print()
    ask_option = input("Please enter an estimate number: ")
    #uses linear search to check if user input matches estimate number
    for line in myfile:
        if ask_option in line: 
            estimate = (line[0:5])
            date = (line[6:16])
            customer_id = (line[17:21])
            final_total = (line[22:25])
            status = (line[26])   
            amt_paid = (line[29])
            #prints all details in suggested format
            print()
            print("The estimate number: ", estimate)
            print("Customer ID: ", customer_id)
            print("The estimate amount: ", final_total)
            print("Estimate date: ", date)
            print("Status: ", status)
            

            
    myfile.close()


#OPTION B

'''
Option B must show all jobs with outstanding payments. 
This only applies to estimates with a status of A (Accepted). 
Payments are outstanding if the amount paid is less than
the final total.
• It must only show outstanding payments for jobs with a status of ‘A’.
• It must calculate and display the total of the outstanding payments.
• Here is a suggested format for displaying the data.
'''
def optionB():
    print("Outstanding payments for jobs: ")
    print()
    with open("paintingjobs.txt") as f:
        list1=f.readlines()
        status_A = "A"
        count = 0
        for lines in list1:
            if status_A in lines:
                print(lines)
                count += 1
                print(count)
    list1.close()
        
    
'''

Option C must calculate the total revenue for jobs that have been accepted and
fully paid.
• The calculation must only include jobs with a status of ‘A’.
• The calculation must only include jobs that have been fully paid.
• Here is a suggested format for displaying the data.
Total Revenue
The company’s total revenue so far is <the total revenue>

'''
#OPTION C
def optionC():
    count = 0
    myfile = open("paintingjobs.txt", "r")
    for record in myfile:
        values = record.split(",")
        #if values[4] == "A":
            
    myfile.close()



#OPTION Q   
def optionQ():
    print("Have a good day! ")
    

#asks user for option with validation check
start_option = input("Please choose an option: ") 
authenticate = "false"
while authenticate == "false":
    if start_option == "A" or start_option == "a":
        optionA()
        authenticate = "true"
        break
    if start_option == "B" or start_option == "b" :
        optionB()
        authenticate = "true"
        break
    if start_option == "C" or start_option == "c":
        optionC()
        authenticate = "true"
        break
    if start_option == "Q" or start_option == "q":
        optionQ()
        authenticate = "true"
        break
        
    else:
        print("Invalid input, please try again. ")
        print()
        start_option = input("Please choose an option: ")
        





