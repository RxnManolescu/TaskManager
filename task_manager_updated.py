import datetime


#loop to read file and store usernames and passwords in dictionary as keys with corresponding values
details_dict = {}
with open ("user.txt", "r") as file:
    text = file.read().splitlines()
    for line in text:
        (key, value) = line.split(", ")
        details_dict[key] = value
 

#function to display menu options for the user that is logged in
def menu(username):
    if username == "admin":
        menu = input('''Select one of the following Options below:
                r  - Registering a user
                a  - Adding a task
                va - View all tasks
                vm - View my task
                ds - Display statistics
                gr - Generate reports
                e  - Exit
                : ''').lower()
        if menu == "r":
            reg_user()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            view_mine(username)
        elif menu == "ds":
            display_statistics()
        elif menu == "gr":
            generate_reports()
        elif menu == "e":
            print("Goodbye!!!")
        else:
            print("Option not recognized! Please try again!")
    else:
        menu = input('''Select one of the following Options below:
                        a  - Adding a task
                        va - View all tasks
                        vm - View my task
                        e  - Exit
                        : ''').lower()
        if menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            view_mine(username)
        elif menu == "e":
            print("Goodbye!!!")
        else:
            print("Option not recognized! Please try again!")


#function to ask user to create new username, new password and do a password check
#then write new details to users list and return user to main menu
def reg_user():
    new_username = input("Please enter a new username: ")
    #check if username already registered
    if new_username in details_dict.keys():
        print("Username already exists. Please try again!")
    else:
        new_password = input("Please create a password: ")
        new_password_check = input("Please confirm password: ")
        #check if passwords match
        if new_password_check == new_password:
            new_user = new_username + ", " + new_password
            print("Success! User registered!")

            with open ("user.txt" , "a") as users:
                users.write("\n" + str(new_user))
        else:
            print("Passwords do not match! Please try again!")
        menu(username)


#function to ask user to assign a new task to an existing user
#user to input a task title, task description,task due date and completion status
def add_task():
    details_dict = {}
    with open ("user.txt", "r") as file:
        text = file.read().splitlines()
        for line in text:
            (key, value) = line.split(", ")
            details_dict[key] = value

    assigned_to = \
        input("Please enter the username to whom the task is assigned: ")
    #check whether user assigned is in the users list or display error if user not found
    if assigned_to in details_dict:
        task_title = input("Please enter the task title: ")
        task_description = input("Please enter the task description: ")
        current_date = datetime.datetime.now().strftime("%d %b %Y")
        task_due_date =\
            input("Please enter the due date in format DD MM YYYY): ").split()
        x = datetime.datetime(year = int(task_due_date[2]),\
            month = int(task_due_date[1]), day = int(task_due_date[0]))
        #variable to store user input of task_due_date in the appropriate date format
        due_date = x.date().strftime("%d %b %Y")
        task_complete = input("Task complete? Yes or No?").lower()
        if task_complete == "yes":
            completion = "Yes"
        elif task_complete == "no":
            completion = "No"
        else:
            print("Please try again!")
        #create new task and write it to the list of tasks
        new_task =", ".join([str(assigned_to), str(task_title),\
            str(task_description), str(current_date), str(due_date),\
            str(completion)])
        
        with open ("tasks.txt", "a") as tasks:
            tasks.write("\n" + str(new_task))
    else:
        print("Assigned username invalid! Please try again!")


#function to read and display all tasks in the "tasks.txt" file
def view_all():
    #read tasks list
    with open ("tasks.txt", "r+") as all_tasks:
        tasks_content = all_tasks.read().splitlines()

        for line in tasks_content:
            tasks = line.split(", ")
            #assign variables to every word in the lines
            task = tasks[1]
            assigned = tasks[0]
            date_assigned = tasks[3]
            due_date = tasks[4]
            task_completion = tasks[5]
            task_descrip = tasks[2]
            #create tasks display and print it out in a user friendly format
            task_display = \
                        "Task:             " + task + "\n"\
                        "Assigned to:      " + assigned + "\n"\
                        "Date assigned:    " + date_assigned + "\n"\
                        "Due date:         " + due_date + "\n"\
                        "Task Complete?    " + task_completion + "\n"\
                        "Task Description: " + task_descrip + "\n"
            print(task_display)


#function to generate users and tasks reports
def generate_reports():
    #open file in read mode
    with open("tasks.txt", "r+") as tasks_file:
        tasks_content = tasks_file.read().splitlines()

        #lists to store tasks data
        tasks_lst = []
        tasks_complete = []
        tasks_incomplete = []
        tasks_incomplete_overdue = []
        tasks_users = []
        current_date = datetime.datetime.today().date()
        
        #loop to check whether tasks have been completed or not and store them into
        #the appropriate lists
        for tasks in tasks_content:
            tasks_lst.append(tasks)
            task = tasks.split(", ")
            tasks_users.append(task[0])
            task[4] = datetime.datetime.strptime(task[4], "%d %b %Y").date()
            #check whther task is complete and add it to the completed tasks list
            if task[5] == "Yes":
                tasks_complete.append(task)
            #check whether task is incomplete and add it to the incompleted tasks list
            elif task[5] == "No":
                tasks_incomplete.append(task)
                #check further whether task is incomplete and overdue and add it to the overdue list
                if task[4] < current_date:
                    tasks_incomplete_overdue.append(task)


        #compile tasks report and print it out in a user friendly manner
        with open("task_overview.txt", "w") as tasks_report:
            tasks_text = f"PLEASE SEE BELOW TASKS REPORT:\n" + "\n" +\
            f"The total number of tasks is: {len(tasks_lst)}" + "\n" +\
            f"The number of tasks completed is: {len(tasks_complete)}" + "\n" +\
            f"The number of incomplete tasks is: {len(tasks_incomplete)}" + "\n" +\
            f"The number of tasks incomplete and overdue is: "\
                f"{len(tasks_incomplete_overdue)}" + "\n" +\
            f"The percentage of tasks that are incomplete is: "\
                f"{round(len(tasks_incomplete)/len(tasks_lst) * 100, 2)} %" + "\n" +\
            f"The percentage of tasks that are overdue is: "\
                f"{round(len(tasks_incomplete_overdue)/len(tasks_lst) * 100, 2)} %" + "\n"
            print(tasks_text, file = tasks_report)

        
        #store all registered users in a list
        registered_users_lst = []

        with open("user.txt", "r+") as users_file:
            users_contents = users_file.read().splitlines()
            
            for user in users_contents:
                users = user.split(", ")
                registered_users_lst.append(users[0])


        #create statement that will be appended to and will be written to user_overview file
        output_statement = f"PLEASE SEE BELOW USERS REPORT!\n\n"\
            f"The total numbers of users is: {len(registered_users_lst)}\n"\
            f"Total number of tasks is {len(tasks_lst)}\n"

        #loop to collect and store users data regarding the 
        #number of tasks assigned/complete/incomplete/overdue
        for users in registered_users_lst:
            user_completed = 0
            user_incomplete = 0
            user_incomplete_overdue = 0
            user_assigned = 0
            for task in tasks_lst:
                tasks = task.split(", ")
                if tasks[0] == users:
                    user_assigned += 1
                    if tasks[-1] == "Yes":
                        user_completed += 1
                    elif tasks[-1] == "No":
                        user_incomplete += 1
                        tasks[4] = datetime.datetime.strptime(tasks[4], "%d %b %Y").date()
                        if tasks[4] < current_date:
                            user_incomplete_overdue +=1
            #append all details to the output_statement
            output_statement += f"\n\t\t{users}:\n"\
                f"Number of tasks assigned: {user_assigned}\n"\

            #conditions to avoid division by 0
            if user_assigned == 0:
                pass
            else:
                output_statement += f"The percentage of total assigned: "\
                        f"{round(user_assigned/len(tasks_lst)*100, 2)} %\n"
                if user_completed == 0:
                    output_statement += f"The percentage assigned completed is 0%\n"
                else:
                    output_statement += f"The percentage assigned completed: "\
                        f"{round(user_completed/user_assigned*100, 2)} %\n"

                if user_incomplete == 0:
                    output_statement += f"The percentage assigned incompleted is 0%\n"
                else:
                    output_statement += f"The percentage assigned incomplete: "\
                        f"{round(user_incomplete/user_assigned*100, 2)} %\n"
                        
                if user_incomplete_overdue == 0:
                    output_statement += f"The percentage assigned incomplete and overdue is 0%\n"
                else:
                    output_statement += f"The percentage assigned overdue: "\
                    f"{round(user_incomplete_overdue/user_assigned*100, 2)} %\n"

        #write report to file
        with open("user_overview.txt", "w") as users_report:
            users_report.write(output_statement)


#function to display all tasks assigned to the user that is logged in
#and allow the user to edit these
def view_mine(username):

    with open("tasks.txt", "r") as file:
        own_tasks = file.read().splitlines()
        task_counter = 0
        all_tasks = []
        task_lst = []

        for line in own_tasks:
            tasks = line.split(", ")
            #append all tasks to the "all_tasks" list
            all_tasks.append(tasks)
            if username == tasks[0]:
                task_counter += 1
                #append all tasks assigned to the user that is signed in to "task_lst"
                task_lst.append(tasks)
                #divide tasks into indices and store them in variables
                task = tasks[1]
                assigned = tasks[0]
                date_assigned = tasks[3]
                due_date = tasks[4]
                task_completion = tasks[5]
                task_descrip = tasks[2]

                #create tasks display and print it out in a user-friendly manner
                task_display = \
                            f"Task number:        {task_counter}" + "\n"\
                            f"Task:               {task}" + "\n"\
                            f"Assigned to:        {assigned}" + "\n"\
                            f"Date assigned:      {date_assigned}" + "\n"\
                            f"Due date:           {due_date}" + "\n"\
                            f"Task Complete?      {task_completion}" + "\n"\
                            f"Task Description:   {task_descrip}" + "\n"
                print(task_display)

        #numbered list of tasks
        numbered_tasks = list(enumerate(task_lst, 1))
        #empty dictionary to store the tasks
        tasks_dict = {}

        #store tasks in dictionary where the keys are the corresponding numbers of the tasks
        for task in numbered_tasks:
            (key, value) = task
            tasks_dict[key] = value

        task_choice = int(input("Please enter the task number or enter \"-1\" for main menu:"))
        #option to return user to main menu
        if task_choice == -1:
            menu(username)
        #options to allow user to only edit the chosen numbered task
        elif task_choice in tasks_dict.keys():
            options1 = int(input("""Please choose from the following options:
                    1 - to mark task as complete
                    2 - to edit task
                    """))
            if options1 == 1:
                #mark any incomplete task as complete or print error message otherwise
                if tasks_dict[task_choice][5] == "No":
                    tasks_dict.get(task_choice)[5] = "Yes"
                    print("This task has now been marked as complete!")
                elif tasks_dict[task_choice][5] == "Yes":
                    print("This task is already complete!")
            elif options1 == 2:
                #options to allow user to edit any incomplete tasks or print error message otherwise
                if tasks_dict[task_choice][5] == "No":
                    options2 = int(input("""Please choose from the following options:
                                1 - to edit the username to whom the task is assigned
                                2 - to edit the due date of the task
                                """))
                    if options2 == 1:
                        #allow user to reassign task to another existing user
                        #or print error message if new user does not exist
                        change_user =\
                            input("Please enter the name to whom the task is to be assigned:")
                        if change_user in details_dict.keys():
                            tasks_dict[task_choice][0] = change_user
                            print("The name assigned to this task has now been updated!")
                        else:
                            print("User not found! Please try again!")
                    elif options2 == 2:
                        #allow user to change the due date of the task
                        task_due =\
                        input("""Please enter the due date in format DD MM YYYY): """).split()
                        x = datetime.datetime(year = int(task_due[2]),\
                            month = int(task_due[1]), day = int(task_due[0]))
                        #variable to store user input of task_due_date in the appropriate date format
                        due_date = x.date().strftime("%d %b %Y")
                        tasks_dict[task_choice][4] = due_date
                        print("The due date for this task has now been updated!")       # ??????????
                    else:
                        print("Option not recognized! Please try again!")
                elif tasks_dict[task_choice][5] == "Yes":
                    print("Sorry, this task has been completed and can no longer be edited!")
            else:
                print("Please try again!")
        else:
            print("Choice not recognised! Please try again!")
        
        #write all user edits to "tasks.txt" file
        with open("tasks.txt", "w") as file:
            [file.write(", ".join(x) + "\n") for x in all_tasks]


#function to display users and tasks statistics
def display_statistics():
    #open file to read data and count number of users
    with open("user.txt", "r") as users_file:
        users_contents = users_file.readlines()
        number_of_users = 0
        for users in users_contents:
            number_of_users += 1

        
    #open file to read and count number of tasks
    with open("tasks.txt", "r") as tasks_file:
        tasks_content = tasks_file.readlines()
        number_of_tasks = 0
        for tasks in tasks_content:
            number_of_tasks += 1

    #print number of users and tasks in a user-friendly manner
    print()
    print(f"The number of users is: {number_of_users}")
    print(f"The number of tasks is: {number_of_tasks}")
    print()
    print("------------------------------------------")
    print()

    #open file to read users report and display it in a user-friendly manner
    with open("user_overview.txt", "r") as user_file:
            text1 = user_file.read().splitlines()
            print("\n".join(text1))
            print()
            print("------------------------------------------")
            print()

    #open file to read tasks report and display it in a user-friendly manner
    with open("task_overview.txt", "r") as task_file:
        text2 = task_file.read().splitlines()
        print("\n".join(text2))
        print("------------------------------------------")
        print()
        print("END OF REPORT!\n")

while True:
    #user to login with their username
    username = input("Please enter your username: ")
    #check whether the username is in the dictionary
    if username in details_dict.keys():
        #if username found, ask user to input password
        password = input("Please enter your password: ")
        #check whether the password corresponds to the username chosen and 
        # allow user to login, print error message otherwise
        if password == details_dict[username]:
            print("\nDetails correct!\n")
            #display menu for user named "admin"
            if username == "admin":
                while True:
                    menu(username)
            #display menu for logged in user that is not "admin"
            else:
                while True:
                    menu(username)
        
        else:
            #print error message if password does not correspond to the username
            print("Password invalid. Please try again!")
                    
    else:
        #print error message if username is not valid
        print("Username invalid! Please try again!")


