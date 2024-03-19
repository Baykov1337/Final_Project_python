To start the project you will need to follow several steps:

1. Prepare your environment:
   I am using Conda. To use the project you'll need it as well.
   Installing conda and config it is not part of the subject.
   To install the requirement packages you will need to do the following commands:
   conda env create -f FinalProject.yaml (with the full path if directory is different in terminal than the project path)

2. The database finances.db - could or could not exist.
   To fully experience the functionality of the project I suggest running /database/create_object.py to to fill with data.

3. To runn the application just execute the app.py  - 
it will start the app on http://127.0.0.1:5000

app.py is main role how the app works.

There are 2 users in the Database - Petar and Boyan. Id for Petar is 2 (you can see the Юзър ID )
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
4. I would like to suggest a feature for the financial report that would allow filtering by start and end date, rather than just by month. I tried using the DateRangeSlider panel for this purpose, but it was time-consuming and I was unable to render HTML or convert the Unix timestamp to a date. I suspect this may be a bug.
5. No testing app code 

Some of the code I've borrowed from other resources.
For the time i had, that's what I've done.
Enjoy using the APP!

Best regards,
Boyan™
