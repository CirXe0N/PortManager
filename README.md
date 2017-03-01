## Port Management System
This is an example project based on an [assignment](#case-description).

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
    DATABASE_HOST: [Hostname of your MySQL Database]
    DATABASE_PORT: 3306
    DATABASE_NAME: port_manager
    DATABASE_USER: [Username of your MySQL Database]
    DATABASE_PASSWORD: [Password of your MySQL Database]
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


### API Information

**Request Header Settings**

Key            | Value                             |
-------------- | --------------------------------- | 
Authorization  | Token [API KEY of a ship captain] | 



**Available Endpoints**


GET /api/v1/ships/{The Ship captains' ship_id or ship_name}

## Case Description
We manage the Rotterdam port. Ships arrive daily. Every ship has a unique identifier, composed of letters and digits. A ship is loaded with containers. Every container has a unique number. It is known whether the contents of a container imply a fire and/or chemical hazard. A ship may enter a dock. A dock can contain only one ship at a time. On every dock, several people are employed, of which some are supervisors. The first name, last name, address and bank account number of each employee is known. Employees are assigned to a ship in the dock.

**Tasks**
* Create a relational database model of the described situation
* Create a web application using Django that implements the following webpages:
    * An overview page that lists docks with their current occupancy and cargo hazards.
    * A dock detail page with for example the employees, current ship, containers and cargo hazards and a historic overview of ships
    * Provide us with a solution that we can run using the Django development server ourselves, to see it in action.

**Bonus assignment**
Based on the application defined for the port management. A third party like the ship-captain would like to enquire the docks for docking possibilities for his ship. The captain uses a system which can handle 3rd party API’s via REST.
Every captain which is listed in our system can authenticate in the ship software using his shipname/code and auth-token. This information is shown on the user profile of the captain accessed via a desktop browser.

Bonus task: Our system should be capable to answer REST requests. Show how this can be implemented.


