## Steps used to build the project ##

1. Used a virtualenv to install the packages used in the project:

        $ pip3 install virtualenv virtualenvwrapper
        $ mkvirtualenv -p $(which python3) expenses-control

        $ pip3 install django djangorestframework


2. Running the server

        # if running for the first time
        $ python3 manage.py makemigrations
        $ python3 manage.py migrate
        $ python3 manage.py createsuperuser

        $ python3 manage.py runserver


3. Testing the endpoints

        # login
        $ curl -H "Content-Type: application/json" --request POST -d '{"username":"admin","password":"admin"}' http://127.0.0.1:8000/api/auth/login/ -v

        # create expense
        $ curl -H "Content-Type: application/json" --request POST -d '{"value": "1450.00", "date": "2018-12-25", "short_desc": "this is a short desc", "long_desc": "this is a long desc"}'  http://127.0.0.1:8000/api/expenses/create/ -H 'Authorization: Token <user_token>' -v

        # get user expenses
        $ curl --request GET http://127.0.0.1:8000/api/expenses/ -H 'Authorization: Token <user_token>' -v

        # get specific user expense
        $ curl --request GET http://127.0.0.1:8000/api/expenses/1/ -H 'Authorization: Token <user_token>' -v

        # create user custom
        $ curl -H "Content-Type: application/json" --request POST -d '{"max_value": "4000.00", "send_notifications": "True"}'  http://127.0.0.1:8000/api/custom/create/ -H 'Authorization: Token <user_token>' -v

        # get user custom
        $ curl --request GET http://127.0.0.1:8000/api/custom/ -H 'Authorization: Token <user_token>' -v
