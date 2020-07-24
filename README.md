#About
* I created an authentication module so multiple users could use the service and track their urls 
* The url shortening service stores the original url and generate another url using the key given by the user or it generates a random string of 6 small letters on its own if the key field is left blank
* There are multiple way to create the key on its own like creating a unique hash_id or hex value of the original url. I used a random string generator as it created fairly unique strings and is easier to check incase of duplicate URLs and also it is easier to control the length of the generated string 



#Setting up 
####run the following commands in order
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

#####This runs the url shortening service on the localhost:8000
#####Follow the steps to create a shortURL
* signup and create an account
* login with your registered email id
* go to the dashboard and paste your url there 
* Either provide your own key or leave it blank to generate a random key
* select whether the url being created is for single use or not 
* Click the generate button and share the generated URL
* after the created link is used refresh the dashboard page to update the visits
