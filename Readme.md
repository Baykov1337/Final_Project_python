To start the project you will need to follow several steps:

There are a few folders in the project.
1. Database folder contains:
    * create_object.py 
    * finances.py
    * users.py

2. I am using Conda. You need to bind the project to Conda, install the necessary libraries from requirements.txt, and select Python: Select Interpreter to be able to use the them all.
    To install requirements you need to execute the following statement in terminal 
    conda install --file requirements.txt
p.s. there are several requirements that are not required, but they come with the packages.

p.p. conda create --name PythonProject
    conda activate PythonProject ( need to be in PS )
    to check : conda info --envs 
                PythonProject         *  C:\Users\Boyan\.conda\envs\PythonProject
    conda install --yes --file requirements.txt 
    conda update --all



The database has already filled with the data, but you can Run the create_objects.py to create the database and fill it with simple data:
It is recommended to do so to see the functionalities of the application.
Simply execute the create_objects.py

The web folder contains CSS, javascript, HTML and images required for the application to function as it should. 
The templates folder is inside the web folder - since we use Flask it is required for the HTML to run successfully.
    header.html - is the main webpage it loads some CSS and redirects to different webpages - since this project is for ITAcademy Stara Zagora you can find all of the necessary information to the Academy on this webpage ( facebook, phone, contacts and resources ). 
    The webpage redirects to different URLs depending on the requirements you need to perform. 

footer.html is part of the main page.

index.html is basicaly home page - it is static with some pictures. 

index2.html - contais data for the financical report - it can filter the data by user and by date range - filtered by months. 

index3.html - manipulates the Income - could be filtered by FirstName and Lastname of the user, There you can insert, update , delete data (crud)

index4.html - manipulates the Expenses - could be filtered by FirstName and Lastname of the user, There you can insert, update , delete data (crud)

app.py is main role how the app works.


To use the app simply start the app.py file in terminal - it will start the app on http://127.0.0.1:5000 
There are 4 tabs - 
Home 
Finance report
Edit Income
Edit Expenses 

There are 2 users in the Database - Petar and Boyan. Id for Petar is 2  (you can see the Юзър ID )
Id for Boyan is 1 
To overview the financial status of each user you can enter into "Финансов Отчет' - there, you can filter by name and by time range ( filtered by months)
To edit financial Income - (манипулация на приходи ), и добавяне на нови хора в базата ( if user does not have income or expenses for any period of time it is deleted from users table. ) 
You can make changes to the existing data by editing or deleting it, or by adding new data. In case the User ID is not already present in the income or expenses, you can add a new one. Please note that if you enter a different name for an existing User ID, it will not create a new user. Instead, it will add a new record for the existing user.
However, if you create a new ID with the same name - the User report will not filter it ( I could make a unique FirstName and LastName in the user table but that also could be solved as a problem when implementing of Login Page)
The same applies to the Expenses tab (Манипулация на разходи)


Basically that's it. 
Enjoy using the webpage I've created 


p.s. 
Stuff that obviously are missing or incomplete:) 
1. Login page - users table could contain the email and password for login didnt had the time to do that.   
    We do not want other people to review our finance balance 
2. The "Insert Data" feature is not very user-friendly as it requires you to manually enter the user_id for a specific person. This can be a challenge if you have multiple users, but implementing a login system could solve that problem. In any case, you can find the "User ID" to identify the specific person 
3. Expenses and Income manipulation could benefit from a Month filter. Additionally, pagination of the data could avoid the need for scrolling down rows if there are too many.
4. Financial report - could be made by start date ( date as a datetime ) and end date - not by month to filter different time ranges - that took me A LOT OF TIME using the panel DateRangeSlider, and I still couldn't figure out how to render HTML and convert unix timestamp to date in panel, could be a bug. PAIN IN THE @$$!
6. No testing app ,code

p.s. 2 Some of the code I've borrowed from other resources. 
For the time i had, that's what I've done. 
Enjoy using the APP!

Best regards, 
Boyan Baykov ™ 
