# Python-Django

(1) what the app is about
This Project is about Shortning Url which can very big at times.
In this project you would be able to share your url by using only small amount of characters.
it can be very usefull at places where user have limited amount to characters to be used (eg. Twitter)


(2) Any assumptions while planning and developing your solution
It  have Api integrations for futhure use
it generate 5 character unique code which cant be reused and does'nt take same Url again
As far now we can create 15787200 unique characters (i.e 15787200 unique url)
if the number of users grow and we can add numeric value and special character which will increincreasese the number by huge margib


(3) how devloper should pull, build, deploy and run the app on their laptop.
1. Install python and  pip
2. Install pip
3. create a Virtual enviroment using python - m venv "venv_name" cd through venv_name directory
4. Activate the virtual enviroment "source bin/activate"
5. Install req.txt file through pip
6. download Project and place it in your Virtual enviroment
7. create superuser so that you can acces admin using python manage.py createsuperuser
8. Make migrations using python manage.py makemigrations
9. Run Migrate python manage.py migrate
10. Start the development server using python manage.py runserver
11. Open localhost:8000 on your browser to view the app
12. Submmit a url to get a shorten Url (you will recive 5 character tokeb)
13. Access thhe shorten url by pasting that token after http://127.0.0.1:8000/

