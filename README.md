# WEB APP FOR CHAT as agent and customer

TECH STACK : Python Django

Requirements: Python on computer

Installation Begin

Downlaod the code or use url of repo

# Step 1 : Install Requirements by cd into mysite folder:
$ pip install -r requirements.txt

# Step 2 : Make sure you are in same directory as manage.py and run command

$ python manage.py migrate -> for database 

# Step 3 : Create admin username and pass in terminal , make sure you are in project directory

$ python manage.py createsuperuser 
-> for dashboard to see messages and rooms whom all users are attached
in custom user

-> dashboard login

-> http://localhost:8000/admin


# Step 4:
$ python manange.py runserver

# Step 5 : Go to
- http:localhost:8000/chat/


Choose agent or customer

IF YOU CHOOSE AGENT 
- you will see page where all the unread messages are shown

IF YOU CHOOSE CUSTOMER
- you will chat box for sending message
- send a message

OPEN OTHER INCOGNITO WINDOW :
- choose agent and you will see undread message from other side
- when you click then you will be the one who will chat no one will enter in your chat






  
