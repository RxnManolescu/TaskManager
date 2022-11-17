# Task Manager

System Managing programs are used widely in order to allow businesses to retrieve and manipulate specific data.
## Project Description
This project allows a business to manage tasks assigned to each member of the team.
## Features:
* The user is prompted to enter their username and password in order to login and the program allows access to the Task system only after validating the credentials. Should the credentials be wrong, the user will attempt again. When logged in, a menu is displayed. 
* The user then has the options of *adding a task* by specifying the user to whom the task is to be assigned, *view all tasks* where the user is able to view all tasks assigned to all team members, *view own tasks* which allows user to view only the tasks that relate to themselves.
* If the logged in username is **"admin"**, additional options are available such as *registering new user* by providing new login credentials, and *display statistics* where a list of *total number of tasks* and *total number of users* is displayed in a user-friendly manner.

## Coding aspects
* two .txt files have been used as databases for the users list and the tasks list
* the **"datetime"** module has been imported in order to specify when *a task is due* and when it was initially *assigned*
* this program has been created with the help of a *dictionary* to retrieve information
* the **entire** program has been created with the help of *while* and *for* loops and *if-else* statements

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
