This is simple django framework base application(Movie application)
Steps To Run the Project:
1) clone project
2) setup virtualenv (install requirement.txt file)
3) python manage.py migrate
4) python manage.py runserver

To add data into Table:
you can use django admin panel
step to create super user
1) python manage.py createsuperuser(username and password)

** admin URL: http://{{domain}}/admin-->(for local url ex-->http://localhost:8000/admin)
after adding data into table
To get Movie List:
URL : http://{{domain}}/movies --->(for local url ex-->http://localhost:8000/movies)

Due to lack of time. I have create a simple application.
I have kept setting file as main configuration file.
We can read configuration in many ways.

