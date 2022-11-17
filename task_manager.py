import datetime

#empty dictionary to store usernames and passwords as keys with corresponding values
details_dict = {}
#open file in reading mode
with open ("user.txt", "r") as file:
    #split text into lines
    text = file.read().splitlines()
    for line in text:
        #split lines into keys and values at every ", "
        (key, value) = line.split(", ")
        #add keys and values to dictionary details_dict
        details_dict[key] = value
 
#print (details_dict)

while True:
    #ask user to login with their username
    username = input("Please enter your username: ")
    #if statement to check whether the username is in the dictionary
    if username in details_dict.keys():
        #if username in dictionary, ask user to input password
        password = input("Please enter your password: ")
        #if statement to check whether the password corresponds to the username inputted
        if password == details_dict[username]:
            #print success message
            print("\nDetails correct!\n")
            #print menu options for user
            if username == "admin":
                while True:
                    menu = input('''Select one of the following Options below:
                            r - Registering a user
                            a - Adding a task
                            va - View all tasks
                            vm - View my task
                            s - Statistics
                            e - Exit
                            : ''').lower()
                    if menu == "r":
                            #ask user to create new username, new password and password check
                            new_username = input("Please enter a new username: ")
                            new_password = input("Please create a password: ")
                            new_password_check = input("Please confirm password: ")
                            #if the new password and new password confirmation match
                            if new_password_check == new_password:
                                #create new user details
                                new_user = new_username + ", " + new_password
                                #write new user details to user.txt file
                                with open ("user.txt" , "a") as users:
                                    users.write("\n" + str(new_user))
                            else:
                                #print message if new password and new password check do not match
                                print("Passwords do not match! Please try again!")
                    elif menu == "a":
                        #ask user to input a user to whom a task will be assigned
                        assigned_to = \
                            input("Please enter the username to whom the task is assigned: ")
                        #check whether user assigned is in the users list
                        if assigned_to in details_dict:
                            #if username is in users list, ask user to input a task title,
                            #task description, task due date
                            task_title = input("Please enter the task title: ")
                            task_description = input("Please enter the task description: ")
                            #print current date
                            current_date = datetime.datetime.now().strftime("%d %b %Y")
                            #ask user to input the task due date and split input at every " "
                            task_due_date =\
                                input("Please enter the due date in format DD MM YYYY): ").split()
                            #variable to store user input into indices for day, month and year
                            x = datetime.datetime(year = int(task_due_date[2]),\
                                month = int(task_due_date[1]), day = int(task_due_date[0]))
                            #variable to store user input in the appropriate date format
                            due_date = x.date().strftime("%d %b %Y")
                            #ask user to input whether the task is complete or not
                            #and print message accordingly
                            task_complete = input("Task complete? Yes or No?").lower()
                            if task_complete == "yes":
                                completion = "Yes"
                            elif task_complete == "no":
                                completion = "No"
                            else:
                                print("Please try again!")
                            #create a new task to include user to whom task has been assigned,
                            #task name, task description, current date, due date and
                            #whether task is completed or not
                            new_task =", ".join([str(assigned_to), str(task_title),\
                                str(task_description), str(current_date), str(due_date),\
                                str(completion)])
                            #write new task to the list of tasks
                            with open ("tasks.txt", "a") as tasks:
                                tasks.write("\n" + str(new_task))
                            #break
                        else:
                            #print error message is assigned user does not exist
                            print("Assigned username invalid! Please try again!")

                    elif menu == "va":
                        #read tasks list
                        with open ("tasks.txt", "r+") as all_tasks:
                            #split tasks list into lines
                            tasks_content = all_tasks.read().splitlines()

                            for line in tasks_content:
                                #split lines into words separated at ", "
                                words = line.split(", ")
                                #assign variables to every word in the lines
                                task = words[1]
                                assigned = words[0]
                                date_assigned = words[3]
                                due_date = words[4]
                                task_completion = words[5]
                                task_descrip = words[2]
                                #display all tasks in a user friendly format
                                task_display = \
                                            "Task:             " + task + "\n"\
                                            "Assigned to:      " + assigned + "\n"\
                                            "Date assigned:    " + date_assigned + "\n"\
                                            "Due date:         " + due_date + "\n"\
                                            "Task Complete?    " + task_completion + "\n"\
                                            "Task Description: " + task_descrip + "\n"
                                #display taks to user
                                print(task_display)

                    elif menu == "vm":
                        #read tasks list
                        with open("tasks.txt", "r") as file:
                            #split list into lines
                            own_tasks = file.read().splitlines()

                            for line in own_tasks:
                                #split lines into words at every ", "
                                words = line.split(", ")
                                #check whether the user that is logged in coincides with the user
                                #to whom the task is assigned
                                if username == words[0]:
                                    #assign variables to every word in the lines
                                    task = words[1]
                                    assigned = words[0]
                                    date_assigned = words[3]
                                    due_date = words[4]
                                    task_completion = words[5]
                                    task_descrip = words[2]
                                    #display in a user friendly manner only the tasks assigned to
                                    #the user that is currently logged in
                                    task_display = \
                                                "Task:             " + task + "\n"\
                                                "Assigned to:      " + assigned + "\n"\
                                                "Date assigned:    " + date_assigned + "\n"\
                                                "Due date:         " + due_date + "\n"\
                                                "Task Complete?    " + task_completion + "\n"\
                                                "Task Description: " + task_descrip + "\n"
                                    #display task to user
                                    print(task_display)

                    elif menu == "s":
                        while True:
                            #open file in read mode
                            with open("user.txt", "r") as users_file:
                                #split txt file into lines
                                contents = users_file.readlines()
                                #declare counter variable
                                number_of_users = 0
                                for i in contents:
                                    #increment counter variable at every pass of the loop
                                    number_of_users += 1
                                
                            #open file in read mode
                            with open("tasks.txt", "r") as tasks_file:
                                #split txt file into lines
                                content = tasks_file.readlines()
                                #declare counter variable
                                number_of_tasks = 0
                                for j in content:
                                    #increment counter variable at every pass of the loop
                                    number_of_tasks += 1
                                break
                        #print number of users
                        print("The number of users is:", number_of_users)
                        #print number of tasks
                        print("The number of tasks is:", number_of_tasks)

                    elif menu == "e":
                        #print message
                        print('Goodbye!!!')
                        exit()

                    else:
                    #print error message if user input doesn't correspond to the choices in the menu
                        print("You have made a wrong choice, Please Try again")
            else:
                while True:
                    menu = input('''Select one of the following Options below:
                            a - Adding a task
                            va - View all tasks
                            vm - View my task
                            e - Exit
                            : ''').lower()
                    if menu == "a":
                        #ask user to input a user to whom a task will be assigned
                        assigned_to = \
                            input("Please enter the username to whom the task is assigned: ")
                        #check whether user assigned is in the users list
                        if assigned_to in details_dict:
                            #if username is in users list, ask user to input a task title,
                            #task description, task due date
                            task_title = input("Please enter the task title: ")
                            task_description = input("Please enter the task description: ")
                            #print current date
                            current_date = datetime.datetime.now().strftime("%d %b %Y")
                            #ask user to input the task due date  and split at every " "
                            task_due_date = \
                                input("Please enter the due date in format DD MM YYYY): ").split()
                            #variable to store user input into indices for day, month and year
                            x = datetime.datetime(year = int(task_due_date[2]),\
                                month = int(task_due_date[1]), day = int(task_due_date[0]))
                            #variable to store user input in the appropriate date format
                            due_date = x.date().strftime("%d %b %Y")
                            #ask user to input whether the task is complete or not
                            #and print message accordingly
                            task_complete = input("Task complete? Yes or No?").lower()
                            if task_complete == "yes":
                                completion = "Yes"
                            elif task_complete == "no":
                                completion = "No"
                            else:
                                print("Please try again!")
                            #create a new task to include user to whom task has been assigned,
                            #task name, task description, current date, due date and
                            #whether task is completed or not
                            new_task =", ".join([str(assigned_to), str(task_title),\
                                str(task_description), str(current_date), str(due_date),\
                                str(completion)])
                            #write new task to the list of tasks
                            with open ("tasks.txt", "a") as tasks:
                                tasks.write("\n" + str(new_task))
                        else:
                            #print error message is assigned user does not exist
                            print("Assigned username invalid! Please try again!")

                    elif menu == "va":
                        #read tasks list
                        with open ("tasks.txt", "r+") as all_tasks:
                            #split tasks list into lines
                            tasks_content = all_tasks.read().splitlines()

                            for line in tasks_content:
                                #split lines into words separated at ", "
                                words = line.split(", ")
                                #assign variables to every word in the lines
                                task = words[1]
                                assigned = words[0]
                                date_assigned = words[3]
                                due_date = words[4]
                                task_completion = words[5]
                                task_descrip = words[2]
                                #display all tasks in a user friendly format
                                task_display = \
                                            "Task:             " + task + "\n"\
                                            "Assigned to:      " + assigned + "\n"\
                                            "Date assigned:    " + date_assigned + "\n"\
                                            "Due date:         " + due_date + "\n"\
                                            "Task Complete?    " + task_completion + "\n"\
                                            "Task Description: " + task_descrip + "\n"
                                #display task to user
                                print(task_display)

                    elif menu == "vm":
                        #read tasks list
                        with open("tasks.txt", "r") as file:
                            #split list into lines
                            own_tasks = file.read().splitlines()

                            for line in own_tasks:
                                #split lines into words at every ", "
                                words = line.split(", ")
                                #check whether the user that is logged in coincides with the user
                                #to whom the task is assigned
                                if username == words[0]:
                                    #assign variables to every word in the lines
                                    task = words[1]
                                    assigned = words[0]
                                    date_assigned = words[3]
                                    due_date = words[4]
                                    task_completion = words[5]
                                    task_descrip = words[2]
                                    #display only the tasks assigned to the user 
                                    #that is currently logged in
                                    task_display = \
                                                "Task:             " + task + "\n"\
                                                "Assigned to:      " + assigned + "\n"\
                                                "Date assigned:    " + date_assigned + "\n"\
                                                "Due date:         " + due_date + "\n"\
                                                "Task Complete?    " + task_completion + "\n"\
                                                "Task Description: " + task_descrip + "\n"
                                    #display task to user
                                    print(task_display)

                    elif menu == "e":
                        #print message
                        print('Goodbye!!!')
                        exit()

                    else:
                    #print error message if user input doesn't correspond to the choices in the menu
                        print("You have made a wrong choice, Please Try again")
        
        else:
            #print error message if password does not correspond to the username
            print("Password invalid. Please try again!") 
                    
    else:
        #print error message if username is not valid
        print("Username invalid! Please try again!")
    


#Asked mentor Neil for help with reading user input into the appropriate date format

