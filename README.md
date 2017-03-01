## Port Management System
This is an example project based on an assignment.

**Notes**: 
* This application has been developed and tested on [Python 3.52](https://www.python.org/downloads/)
* Passwords and sensitive settings are uploaded for **educational** purposes! This should **never** be done in real projects!
* If you start with **Docker**, skip the sections: **Installation(Manual)** and **Usage(Manual)**

### Prerequisites
* [Python 3.52](https://www.python.org/downloads/)
* [MySQL 5.7+](https://dev.mysql.com/downloads/mysql/)
* [Virtualenv 15+](https://virtualenv.pypa.io/en/stable/installation/)

**Optional:**
* [Docker](https://docs.docker.com/engine/installation/)
* [Docker-compose](https://docs.docker.com/compose/install/)

### Installation (Manual)
1. Create a virtualenv container and activate it. For more information: [Click here](https://virtualenv.pypa.io/en/stable/userguide/#usage)
2. Open Terminal and change to the directory of the project.
3. Install the dependencies of the project by entering the following command:
    
    ```
    $ pip install -r requirements.txt
    ```

4. Make sure the MySQL Server is up and running.
5. Create a database called **'port_manager'**.
6. In the project folder create a file **parameters.yml** and enter the following data:
   ```
    ENVIRONMENT: LOCAL
    SECRET_KEY: '&i4hv(y#kh6yl=s5jls&-@)5h!8t!8p^rkr0=p9f7oswvlw8#@'
    DATABASE_HOST: mysql
    DATABASE_PORT: 3306
    DATABASE_NAME: port_manager
    DATABASE_USER: [username of your local database]
    DATABASE_PASSWORD: [password of your local database]
   ```
7. Save the file. 
8. Run the following commands to setup database schema and to create dummy data:
     
    ```
    $ python ./manage.py migrate --noinput
    $ python ./manage.py createdefaultuser
    $ python ./manage.py loaddummydata
    ```

### Usage (Manual)
1. Run the following command to run the web server:
   
    ```
    $ python ./manage.py runserver 0.0.0.0:8000
    ```
2. Open web browser and go to: [http://localhost:8000](http://localhost:8000/)


### Installation (Docker)
1. Open Terminal and change to the directory of the project.
    ```
    $ sudo chmod +x run_web.sh
    ```

### Usage (Docker)
1. Run the following command to start the docker containers:
    ```
    $ sudo docker-compose up
    ```
2. Wait for the containers to start up.
3. Open web browser and go to: [http://localhost:8000](http://localhost:8000/)



### Login Information
User          | Username                  | Password     | URL
------------- | ------------------------- | -------------| ---------------  
Super Admin   | admin                     | test         | [Admin Page](http://localhost:8000/admin)
Ship Captains | _[email_address of user]_ | test         | [Main Page](http://localhost:8000/)