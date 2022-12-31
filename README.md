# University of Toronto - Google Developer Student Club Signup App
As a member of UofT's GDSC, I designed this signup app that allows members to join the club and become a member. This signup app is implemented using Python's Django Framework while HTML and CSS were used to design the webpages. <br />

![Quote](https://github.com/kannikakabilar/UofT-Club-Signup-App/blob/main/screenshots/Screen%20Shot%202022-12-29%20at%2010.00.29%20PM.png)
<br />
![Quote](https://github.com/kannikakabilar/UofT-Club-Signup-App/blob/main/screenshots/Screen%20Shot%202022-12-29%20at%2010.00.45%20PM.png)
<br />
![Quote](https://github.com/kannikakabilar/UofT-Club-Signup-App/blob/main/screenshots/Screen%20Shot%202022-12-29%20at%2010.01.16%20PM.png)
<br />
# Features
Students can join the club by providing their uoft email and they will be added to sqlite database. Their records can be additionally connected to their unique student number.
<br />
![Quote](https://github.com/kannikakabilar/UofT-Club-Signup-App/blob/main/screenshots/Screen%20Shot%202022-12-31%20at%201.19.16%20PM.png)
<br />
All members of the club can be viewed here along with their subjects of interest and their role in the club. Only the admin can modify the role of a club member. By default, a new member will be assigned as a developer. Students can view what subjects within computer science the other members are interested in and can collobarate with them to work on startup ideas and projects.
<br />
![Quote](https://github.com/kannikakabilar/UofT-Club-Signup-App/blob/main/screenshots/Screen%20Shot%202022-12-29%20at%2010.01.07%20PM.png)
<br />
Students can edit and view their profile when they can correctly provide their private id number. They can also leave the club which will remove their record from the club's database.
<br />
![Quote](https://github.com/kannikakabilar/UofT-Club-Signup-App/blob/main/screenshots/Screen%20Shot%202022-12-31%20at%201.19.32%20PM.png)
<br />
Admins are given full control and can modify any records in the database.
<br />
![Quote](https://github.com/kannikakabilar/UofT-Club-Signup-App/blob/main/screenshots/Screen%20Shot%202022-12-29%20at%209.59.50%20PM.png)
<br />
<br />
# How To Run
- Requirements; the following needs to be installed
```md
> python3 --version
> pip --version
```
- Using an existing virtual environment with test records <br />
Navigate to the application's directory and type the following commands. 
```md
> source bin/activate
> python3 manage.py runserver
``` 
<br />
Go to: http://127.0.0.1:8000/members/
<br />
<br />
* Running it from scratch <br />
Navigate to the application's directory and type the following commands. <br /> 
<br />
<br /> 
```md
> python3 -m venv myvirenv <br />
> source myvirenv/bin/activate <br />
> python3 -m pip install Django <br />
> python3 manage.py makemigrations members <br />
> python3 manage.py migrate <br />
> python3 manage.py runserver <br /> 
``` 
<br />
<br />
Go to: http://127.0.0.1:8000/members/
<br />
<br />
** Create a superuser for admin purposes. ** <br />
<br />
> python3 manage.py createsuperuser
<br />
<br />
Go to: http://127.0.0.1:8000/admin
<br /> 
<br />
